from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderListSerializer


class OrderListView(APIView):
    """Вывод списка клиентов"""
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)
