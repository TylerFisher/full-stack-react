from fullstack.models import Party
from rest_framework import serializers


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"
