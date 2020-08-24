from rest_framework import serializers

from .models import Order


class OrderListSerializer(serializers.ModelSerializer):
    """Список клиентов"""

    class Meta:
        model = Order
        fields = ("status", "date_start", "date_end", "id_client", "id_apartment")


class OrderDetailSerializer(serializers.ModelSerializer):
    """Подробный вывод по одному клиенту"""

    class Meta:
        model = Order
        fields = ("status", "date_start", "date_end", "timestamp", "id_client", "id_apartment")
