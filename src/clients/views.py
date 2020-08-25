from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .serializers import ClientListSerializer, ClientDetailSerializer


class ClientListView(APIView):
    """Вывод списка клиентов"""
    def get(self, request):
        """Получение списка клиентов"""
        clients = Client.objects.all()
        serializer = ClientListSerializer(clients, many=True)
        return Response(serializer.data)


class ClientDetailView(APIView):
    """Детальный вывод по одному клиенту"""
    def get(self, request, pk):
        """Получение одной записи по ID"""
        client = Client.objects.get(id=pk)
        serializer = ClientDetailSerializer(client)
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
