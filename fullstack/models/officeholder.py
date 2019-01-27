import uuid

from django.db import models

from .person import Person
from .office import Office
from .party import Party


class Officeholder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    party = models.ForeignKey(
        Party, on_delete=models.SET_NULL, null=True, blank=True
    )
    term_start = models.DateField()
    term_end = models.DateField()

    def __str__(self):
        return "{}, {}, {}-{}".format(
            self.person.full_name,
            self.office.label,
            self.term_start.strftime("%Y"),
            self.term_end.strftime("%Y"),
        )
