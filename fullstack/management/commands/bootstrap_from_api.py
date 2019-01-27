import csv
import os
import requests
import us

from datetime import datetime
from django.core.management.base import BaseCommand
from django.contrib.humanize.templatetags.humanize import ordinal
from fullstack.models import (
    Body,
    Division,
    DivisionLevel,
    Office,
    Officeholder,
    Party,
    Person,
)
from tqdm import tqdm

BASE_URL = "https://api.propublica.org/congress/v1"
API_PARTY_MAP = {"R": "Republican", "D": "Democrat", "ID": "Independent"}


class Command(BaseCommand):
    def create_division_levels(self):
        self.country, created = DivisionLevel.objects.get_or_create(
            name=DivisionLevel.COUNTRY
        )

        self.state, created = DivisionLevel.objects.get_or_create(
            name=DivisionLevel.STATE, parent=self.country
        )

        self.county, created = DivisionLevel.objects.get_or_create(
            name=DivisionLevel.COUNTY, parent=self.state
        )

        self.district, created = DivisionLevel.objects.get_or_create(
            name=DivisionLevel.DISTRICT, parent=self.state
        )

        self.township, created = DivisionLevel.objects.get_or_create(
            name=DivisionLevel.TOWNSHIP, parent=self.county
        )

        self.precinct, created = DivisionLevel.objects.get_or_create(
            name=DivisionLevel.PRECINCT, parent=self.county
        )

    def create_divisions(self, f, districts_per_state):
        usa, created = Division.objects.get_or_create(
            name="United States of America",
            label="United States of America",
            short_label="USA",
            level=self.country,
        )

        for state in us.states.STATES:
            f.seek(0)
            this_state, created = Division.objects.get_or_create(
                name=state.name,
                label=state.name,
                short_label=state.abbr,
                code=state.fips,
                parent=usa,
                level=self.state,
            )

            for district_state in districts_per_state:
                if district_state["state"] == state.name:
                    num_districts = int(district_state["districts"])

            if num_districts == 1:
                Division.objects.get_or_create(
                    name="{} at-large congressional district".format(
                        state.name
                    ),
                    label="{} at-large congressional district".format(
                        state.name
                    ),
                    short_label="{}-AL".format(state.abbr),
                    code="{}-AL".format(state.abbr),
                    parent=this_state,
                    level=self.district,
                )
            else:
                for x in range(1, num_districts + 1):
                    Division.objects.get_or_create(
                        name="{} {} congressional district".format(
                            state.name, ordinal(x)
                        ),
                        label="{} {} congressional district".format(
                            state.name, ordinal(x)
                        ),
                        short_label="{}-{}".format(
                            state.abbr, str(x).zfill(2)
                        ),
                        code="{}-{}".format(state.abbr, str(x).zfill(2)),
                        parent=this_state,
                        level=self.district,
                    )

    def build_congressional_offices(self, chamber):
        r = requests.get(
            "{0}/{1}/{2}/members.json".format(BASE_URL, "116", chamber),
            headers={
                "X-API-Key": os.environ.get("PROPUBLICA_CONGRESS_API_KEY")
            },
        )

        members = r.json()

        print("Loading U.S. {0} offices".format(chamber.title()))
        for member in tqdm(members["results"][0]["members"]):
            full_state = us.states.lookup(member["state"])
            if int(full_state.fips) > 56 or int(full_state.fips) == 11:
                continue

            if chamber == "senate":
                for class_tup in Office.SENATE_CLASSES:
                    if class_tup[0] == member["senate_class"]:
                        senate_class = class_tup[0]

                name = "U.S. Senate, {0}, Class {1}".format(
                    full_state.name, senate_class
                )
                division = Division.objects.get(
                    level=self.state, short_label=member["state"]
                )

            elif chamber == "house":
                senate_class = None

                name = "U.S. House, {0}, District {1}".format(
                    full_state.name, member["district"]
                )

                if member["at_large"]:
                    code = "{}-AL".format(member["state"])
                else:
                    code = "{}-{}".format(
                        member["state"], member["district"].zfill(2)
                    )

                division = Division.objects.get(level=self.district, code=code)

            body = Body.objects.get(slug=chamber)

            office, created = Office.objects.get_or_create(
                name=name,
                label=name,
                division=division,
                body=body,
                senate_class=senate_class,
            )

            print(member["last_name"], member["party"])
            party = Party.objects.get(label=API_PARTY_MAP[member["party"]])

            person, created = Person.objects.get_or_create(
                first_name=member["first_name"],
                last_name=member["last_name"],
                gender=member["gender"],
            )

            if chamber == "senate":
                if not member.get("next_election"):
                    term_start = 2018
                    term_end = 2020
                else:
                    term_start = int(member["next_election"]) - 6
                    term_end = int(member["next_election"])

            else:
                term_start = 2018
                term_end = int(member["next_election"])

            Officeholder.objects.get_or_create(
                office=office,
                party=party,
                person=person,
                term_start=datetime(term_start, 1, 1),
                term_end=datetime(term_end, 1, 1),
            )

    def handle(self, *args, **options):
        Body.objects.get_or_create(
            slug="senate", label="U.S. Senate", short_label="Senate"
        )
        Body.objects.get_or_create(
            slug="house",
            label="U.S. House of Representatives",
            short_label="U.S. House",
        )

        print("Loading political parties")

        Party.objects.get_or_create(label="Republican", short_label="GOP")

        Party.objects.get_or_create(label="Democrat", short_label="Dem")

        Party.objects.get_or_create(label="Libertarian", short_label="Lib")

        Party.objects.get_or_create(label="Green", short_label="GP")

        Party.objects.get_or_create(label="Independent", short_label="Ind")

        self.create_division_levels()

        cmd_path = os.path.dirname(os.path.realpath(__file__))
        csv_path = os.path.join(cmd_path, "../../bin/districts.csv")

        with open(csv_path) as f:
            districts_per_state = csv.DictReader(f)
            self.create_divisions(f, districts_per_state)

        for chamber in ["senate", "house"]:
            self.build_congressional_offices(chamber)
