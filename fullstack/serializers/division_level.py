from fullstack.models import DivisionLevel
from rest_framework import serializers


class DivisionLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionLevel
        fields = "__all__"
