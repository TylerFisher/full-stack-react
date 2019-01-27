from fullstack.models import Party
from fullstack.serializers import PartySerializer

from .base import BaseViewSet


class PartyViewSet(BaseViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
