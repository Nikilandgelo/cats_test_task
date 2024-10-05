from rest_framework.viewsets import ModelViewSet
from cats.models import Cat, UsersCatsScore
from cats.serializers import CatSerializer
from cats_project.custom_permissions import IsOwnerOrReadOnly
from cats.filters import CatsFilter
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from drf_spectacular.utils import (extend_schema, OpenApiResponse,
                                   OpenApiExample)
from drf_spectacular.types import OpenApiTypes


class CatsViewSet(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [IsOwnerOrReadOnly(['owner'])]
    filterset_class = CatsFilter

    @extend_schema(
        request={'application/json': OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                'Example 1',
                value={'score': 1},
                request_only=True,
                media_type='application/json'
            ),
            OpenApiExample(
                'Example 2',
                value={'score': 5},
                request_only=True,
                media_type='application/json'
            )
        ],
        responses={
            200: OpenApiResponse(
                response=str, description='Rate has been set to user`s cat'),
            400: OpenApiResponse(
                response=str, description='Some validation error'),
            404: OpenApiResponse(
                response=str, description='Cat with UUID not found'),
        },
        description=("Rate a specific cat by its ID. Returns 200 if successful"
                     ", 404 if not found or 400 for validation errors.")
    )
    @action(detail=True, methods=['POST'], url_path='rate', url_name='rate')
    def rate_cat(self, request, pk=None):
        cat: Cat = get_object_or_404(Cat, id=pk)
        score = request.data.get('score')
        if score is None:
            return Response('You must pass "score" field', status=400)
        if cat.owner == request.user:
            return Response('You can`t rate your own cat', status=400)
        cat_score = UsersCatsScore(user=request.user, cat=cat, score=score)
        try:
            cat_score.full_clean()
        except ValidationError as err:
            return Response(err.message_dict, status=400)
        cat_score.save()
        return Response(f'Rate {score} has been set to {cat} cat')
