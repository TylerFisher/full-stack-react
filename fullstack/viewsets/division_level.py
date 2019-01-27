from fullstack.models import DivisionLevel
from fullstack.serializers import DivisionLevelSerializer

from .base import BaseViewSet


class DivisionLevelViewSet(BaseViewSet):
    queryset = DivisionLevel.objects.all()
    serializer_class = DivisionLevelSerializer
