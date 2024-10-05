from rest_framework.decorators import api_view
from User.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from drf_spectacular.utils import (extend_schema, OpenApiResponse,
                                   OpenApiExample)
from drf_spectacular.types import OpenApiTypes


@extend_schema(responses={
        201: OpenApiResponse(
            response=str, description='User has been created'),
        400: OpenApiResponse(
            response=str, description='Some validation error'),
    },
    request=UserSerializer)
@api_view(['POST'])
def registration(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.create(serializer.validated_data)
    return Response('User has been created', status=201)


@extend_schema(
        request={'application/json': OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                'Example 1',
                value={
                    'username': 'user1',
                    'password': 'password1',
                },
                request_only=True,
                media_type='application/json'
            )
        ],
        responses={
            200: OpenApiResponse(
                response=str, description='User exists and token is returned'),
            401: OpenApiResponse(
                response=str, description='Invalid credentials'),
        },
        description="Login. Returns 200 if successful, 401 if not."
    )
@api_view(['POST'])
def login(request):
    user = authenticate(**request.data)
    if user is not None:
        return Response(f'Your token is: {user.auth_token.key}', status=200)
    else:
        return Response('Invalid credentials', status=401)
