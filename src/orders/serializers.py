from rest_framework import serializers

from .models import Order


class OrderListSerializer(serializers.ModelSerializer):
    """Список заказов"""

    class Meta:
        model = Order
        fields = ("status", "date_start", "date_end", "id_client", "id_apartment")


class OrderDetailSerializer(serializers.ModelSerializer):
    """Детальный вывод по одному заказу"""
    # TODO Понять почему не работает так как должно работать :|
    # id_client = serializers.SlugRelatedField(slug_field="full_name", read_only=True)
    # id_apartment = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Order
        fields = ("status", "date_start", "date_end", "timestamp", "id_client", "id_apartment")
