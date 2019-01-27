import uuid

from django.db import models
from uuslug import slugify


class DivisionLevel(models.Model):
    """
    Level of government or administration at which a division exists.

    For example, federal, state, district, county, precinct, municipal.
    """

    COUNTRY = "country"
    STATE = "state"
    DISTRICT = "district"
    COUNTY = "county"
    TOWNSHIP = "township"
    PRECINCT = "precinct"

    LEVEL_CHOICES = (
        (COUNTRY, "Country"),
        (STATE, "State"),
        (DISTRICT, "District"),
        (COUNTY, "County"),
        (TOWNSHIP, "Township"),
        (PRECINCT, "Precinct"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    slug = models.SlugField(
        blank=True, max_length=255, unique=True, editable=False
    )

    name = models.CharField(max_length=255, unique=True, choices=LEVEL_CHOICES)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )

    def save(self, *args, **kwargs):
        """
        **uid**: :code:`{levelcode}`
        """
        self.slug = slugify(self.name)
        super(DivisionLevel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
