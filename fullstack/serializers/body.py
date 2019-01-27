from fullstack.models import Body
from rest_framework import serializers


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = "__all__"
