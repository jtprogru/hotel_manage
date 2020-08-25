from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Apartment
from .serializers import ApartmentListSerializer, ApartmentDetailSerializer


class ApartmentListView(APIView):
    """Вывод списка номеров"""
    def get(self, request):
        """Получение списка записей"""
        apartmetns = Apartment.objects.all()
        serializer = ApartmentListSerializer(apartmetns, many=True)
        return Response(serializer.data)


class ApartmentDetailView(APIView):
    """Детальный вывод по одному номеру"""
    def get(self, request, pk):
        """Получение одной записи по ID"""
        apartment = Apartment.objects.get(id=pk)
        serializer = ApartmentDetailSerializer(apartment)
        return Response(serializer.data)

    # def post(self, request, pk):
    #     """Создание одной записи по ID"""
    #     pass
    #
    # def put(self, request, pk):
    #     """Обновление одной записи в БД по ID"""
    #     pass
    #
    # def delete(self, request, pk):
    #     """Удаление одной записи из БД по ID"""
    #     pass
