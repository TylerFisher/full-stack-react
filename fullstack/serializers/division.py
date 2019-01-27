from fullstack.models import Division
from rest_framework import serializers


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = "__all__"
