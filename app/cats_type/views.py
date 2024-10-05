from rest_framework.views import APIView
from cats_type.models import CatsType
from cats_type.serializers import CatsTypeSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class CatsTypeView(APIView):
    
    @extend_schema(responses=CatsTypeSerializer, request=CatsTypeSerializer)
    def get(self, request):
        serializer = CatsTypeSerializer(CatsType.objects.all(), many=True)
        return Response(serializer.data)
