from fullstack.models import Officeholder
from rest_framework import serializers


class OfficeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officeholder
        fields = "__all__"
