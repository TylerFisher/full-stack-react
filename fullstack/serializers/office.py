from fullstack.models import Office
from rest_framework import serializers


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"
