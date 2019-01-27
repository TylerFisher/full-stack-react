from fullstack.models import Person
from fullstack.serializers import PersonSerializer

from .base import BaseViewSet


class PersonViewSet(BaseViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
