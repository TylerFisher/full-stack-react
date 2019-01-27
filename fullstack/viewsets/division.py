from fullstack.models import Division
from fullstack.serializers import DivisionSerializer

from .base import BaseViewSet


class DivisionViewSet(BaseViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
