from rest_framework import serializers
from cats_type.models import CatsType
from drf_spectacular.utils import extend_schema_field, OpenApiTypes


@extend_schema_field(OpenApiTypes.STR)
class CatTypeField(serializers.Field):

    def to_representation(self, value: CatsType) -> str:
        return value.name
    
    def to_internal_value(self, data):
        try:
            return CatsType.objects.get(name=data)
        except CatsType.DoesNotExist:
            raise serializers.ValidationError(
                f"Type of cats {data} doesnt exists")
