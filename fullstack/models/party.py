import uuid

from django.db import models
from uuslug import slugify


class Party(models.Model):
    """
    A political party.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(
        blank=True,
        max_length=255,
        editable=True,
        help_text="Customizable slug. Defaults to slugged Org name.",
    )
    label = models.CharField(max_length=255, blank=True)
    short_label = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = "Parties"

    def save(self, *args, **kwargs):
        """
        **uid**: :code:`party:{apcode}`
        """
        if not self.slug:
            self.slug = slugify(self.label)
        super(Party, self).save(*args, **kwargs)
