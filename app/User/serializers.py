from rest_framework.serializers import ModelSerializer
from User.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
