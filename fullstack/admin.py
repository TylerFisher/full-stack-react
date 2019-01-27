from django.contrib import admin
from fullstack.models import (
    Body,
    Division,
    DivisionLevel,
    Office,
    Officeholder,
    Party,
    Person,
)

admin.site.register(Body)
admin.site.register(Division)
admin.site.register(DivisionLevel)
admin.site.register(Office)
admin.site.register(Officeholder)
admin.site.register(Party)
admin.site.register(Person)
