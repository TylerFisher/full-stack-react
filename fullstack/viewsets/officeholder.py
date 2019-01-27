from fullstack.models import Officeholder
from fullstack.serializers import OfficeholderSerializer

from .base import BaseViewSet


class OfficeholderViewSet(BaseViewSet):
    queryset = Officeholder.objects.all()
    serializer_class = OfficeholderSerializer
