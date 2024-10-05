from rest_framework import serializers
from .models import Cat
from cats_project.serializers_fields import CatTypeField
from django.db.models import Avg


class CatSerializer(serializers.ModelSerializer):
    type = CatTypeField()
    owner = serializers.StringRelatedField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Cat
        fields = ['color', 'age', 'description', 'type', 'owner',
                  'average_rating']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
    
    def get_average_rating(self, obj: Cat) -> float:
        avg: dict = obj.scores.aggregate(average=Avg('score'))
        if avg['average'] is None:
            return 0.0
        return avg['average']
