from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderListSerializer, OrderDetailSerializer


class OrderListView(APIView):
    """Вывод списка клиентов"""
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetailView(APIView):
    """Вывод списка клиентов"""
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)
