# -*- coding: utf-8 -*-
import uuid

from django.db import models
from uuslug import uuslug

from .division_level import DivisionLevel


class Division(models.Model):
    """
    A political or administrative geography.

    For example, a particular state, county, district, precinct or
    municipality.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    slug = models.SlugField(
        blank=True, max_length=255, unique=True, editable=False
    )

    name = models.CharField(max_length=255)

    label = models.CharField(max_length=255, blank=True)
    short_label = models.CharField(max_length=50, null=True, blank=True)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )

    level = models.ForeignKey(
        DivisionLevel, on_delete=models.PROTECT, related_name="divisions"
    )

    code = models.CharField(
        max_length=200,
        help_text="Code representing a geography: FIPS code for states and \
        counties, district number for districts, precinct number for \
        precincts, etc.",
    )

    def save(self, *args, **kwargs):
        """
        **uid**: :code:`division:{parentuid}_{levelcode}-{code}`
        """
        self.slug = uuslug(
            self.name, instance=self, max_length=100, separator="-", start_no=2
        )
        super(Division, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
