from fullstack.models import Office
from fullstack.serializers import OfficeSerializer

from .base import BaseViewSet


class OfficeViewSet(BaseViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
