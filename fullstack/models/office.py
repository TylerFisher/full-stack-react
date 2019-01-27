import uuid

from django.db import models
from fullstack.constants import STOPWORDS
from uuslug import uuslug

from .body import Body
from .division import Division


class Office(models.Model):
    """
    An office represents a post, seat or position occuppied by an individual
    as a result of an election.

    For example: Senator, Governor, President, Representative.

    In the case of executive positions, like governor or president, the office
    is tied directlty to a jurisdiction. Otherwise, the office ties to a body
    tied to a jurisdiction.

    .. note::
        Duplicate slugs are allowed on this model to accomodate states, for
        example:

        - florida/house/seat-2/
        - michigan/house/seat-2/
    """

    FIRST_CLASS = "1"
    SECOND_CLASS = "2"
    THIRD_CLASS = "3"

    SENATE_CLASSES = (
        (FIRST_CLASS, "1st Class"),
        (SECOND_CLASS, "2nd Class"),
        (THIRD_CLASS, "3rd Class"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(blank=True, max_length=255, editable=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255, blank=True)
    short_label = models.CharField(max_length=50, null=True, blank=True)
    senate_class = models.CharField(
        max_length=1, choices=SENATE_CLASSES, null=True, blank=True
    )

    division = models.ForeignKey(
        Division, related_name="offices", on_delete=models.PROTECT
    )
    body = models.ForeignKey(
        Body,
        null=True,
        blank=True,
        related_name="offices",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.label

    @property
    def is_executive(self):
        """Is this an executive office?"""
        return self.body is None

    def save(self, *args, **kwargs):
        """
        **uid**: :code:`{body.uid | jurisdiction.uid}_office:{slug}`
        """
        stripped_name = " ".join(
            w for w in self.name.split() if w not in STOPWORDS
        )

        if not self.slug:
            self.slug = uuslug(
                stripped_name,
                instance=self,
                max_length=100,
                separator="-",
                start_no=2,
            )

        super(Office, self).save(*args, **kwargs)
