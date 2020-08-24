from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .serializers import ClientListSerializer, ClientDetailSerializer


class ClientListView(APIView):
    """Вывод списка клиентов"""
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientListSerializer(clients, many=True)
        return Response(serializer.data)


class ClientDetailView(APIView):
    """Вывод списка клиентов"""
    def get(self, request, pk):
        client = Client.objects.get(id=pk)
        serializer = ClientDetailSerializer(client)
        return Response(serializer.data)
