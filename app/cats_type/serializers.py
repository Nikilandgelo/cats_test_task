from rest_framework import serializers
from .models import CatsType


class CatsTypeSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = CatsType
        fields = ['name', 'cats']
