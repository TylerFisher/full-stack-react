from fullstack.models import Body
from fullstack.serializers import BodySerializer

from .base import BaseViewSet


class BodyViewSet(BaseViewSet):
    queryset = Body.objects.all()
    serializer_class = BodySerializer
