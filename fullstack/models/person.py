import uuid

from django.db import models
from fullstack.fields import GenderField
from uuslug import uuslug
from .party import Party


class Person(models.Model):
    """A real human being.🎵

    Generally follows the Popolo spec:
    http://www.popoloproject.com/specs/person.html
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    slug = models.SlugField(
        blank=True, max_length=255, unique=True, editable=False
    )

    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    suffix = models.CharField(max_length=10, null=True, blank=True)
    full_name = models.CharField(max_length=500, null=True, blank=True)

    gender = GenderField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        **uid**: :code:`person:{slug}`
        """
        if not self.full_name:
            self.full_name = "{0}{1}{2}".format(
                self.first_name,
                "{}".format(
                    " " + self.middle_name + " " if self.middle_name else " "
                ),
                self.last_name,
                "{}".format(" " + self.suffix if self.suffix else ""),
            )

        self.slug = uuslug(
            self.full_name,
            instance=self,
            max_length=100,
            separator="-",
            start_no=2,
        )

        super(Person, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.full_name
