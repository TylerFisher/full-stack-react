import pycountry
import us
from django.db import models


class GenderField(models.CharField):
    def __init__(self, *args, **kwargs):
        MALE = "M"
        FEMALE = "F"
        TRANSGENDER = "T"
        OTHER = "O"
        GENDER_CHOICES = (
            (MALE, "Male"),
            (FEMALE, "Female"),
            (TRANSGENDER, "Transgender"),
            (OTHER, "Other"),
        )
        kwargs["choices"] = GENDER_CHOICES
        kwargs["max_length"] = 1
        super(GenderField, self).__init__(*args, **kwargs)


class RaceField(models.CharField):
    def __init__(self, *args, **kwargs):
        WHITE = "W"
        BLACK = "B"
        HISPANIC = "H"
        ASIAN = "A"
        INDIAN = "I"
        PACIFIC = "P"
        MIXED = "M"
        RACE_CHOICES = (
            (WHITE, "White"),
            (BLACK, "Black"),
            (HISPANIC, "Hispanic"),
            (ASIAN, "Asian"),
            (INDIAN, "American Indian"),
            (PACIFIC, "Pacific Islander"),
            (MIXED, "Mixed-race"),
        )
        kwargs["choices"] = RACE_CHOICES
        kwargs["max_length"] = 1
        super(RaceField, self).__init__(*args, **kwargs)


class StateField(models.CharField):
    def __init__(self, *args, **kwargs):
        STATE_CHOICES = tuple(
            [
                (state.abbr, state.name)
                for state in us.states.STATES_AND_TERRITORIES
            ]
        )
        kwargs["choices"] = STATE_CHOICES
        kwargs["max_length"] = 2
        super(StateField, self).__init__(*args, **kwargs)


class CountryField(models.CharField):
    def __init__(self, *args, **kwargs):
        COUNTRY_CHOICES = tuple(
            [
                (country.alpha_2, country.name)
                for country in list(pycountry.countries)
            ]
        )
        kwargs["choices"] = COUNTRY_CHOICES
        kwargs["max_length"] = 2
        super(CountryField, self).__init__(*args, **kwargs)
