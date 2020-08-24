from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Apartment
from .serializers import ApartmentListSerializer, ApartmentDetailSerializer


class ApartmentListView(APIView):
    """Вывод списка номеров"""
    def get(self, request):
        apartmetns = Apartment.objects.all()
        serializer = ApartmentListSerializer(apartmetns, many=True)
        return Response(serializer.data)


class ApartmentDetailView(APIView):
    """Вывод списка номеров"""
    def get(self, request, pk):
        apartment = Apartment.objects.get(id=pk)
        serializer = ApartmentDetailSerializer(apartment)
        return Response(serializer.data)
