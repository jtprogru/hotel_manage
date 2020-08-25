from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderListSerializer, OrderDetailSerializer


class OrderListView(APIView):
    """Вывод списка заказов"""
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetailView(APIView):
    """Детальный вывод по одному номеру"""
    def get(self, request, pk):
        """Получение одной записи по ID"""
        order = Order.objects.get(id=pk)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)

    # def post(self, request, pk):
    #     """Создание одной записи по ID"""
    #     order = Order.objects.get_or_create(id=pk)
    #     serializer = OrderDetailSerializer(order)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk):
    #     """Обновление одной записи в БД по ID"""
    #     order = Order.objects.get(id=pk)
    #     serializer = OrderDetailSerializer(order)
    #     return Response(serializer.data)
    #
    # def delete(self, request, pk):
    #     """Удаление одной записи из БД по ID"""
    #     order = Order.objects.get(id=pk)
    #     serializer = OrderDetailSerializer(order)
    #     return Response(serializer.data)
