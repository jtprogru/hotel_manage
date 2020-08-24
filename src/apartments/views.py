from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Apartment
from .serializers import ApartmentListSerializer


class ApartmentListView(APIView):
    """Вывод списка номеров"""
    def get(self, request):
        apartmetns = Apartment.objects.all()
        serializer = ApartmentListSerializer(apartmetns, many=True)
        return Response(serializer.data)
