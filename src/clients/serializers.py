from rest_framework import serializers

from .models import Client


class ClientListSerializer(serializers.ModelSerializer):
    """Список клиентов"""

    class Meta:
        model = Client
        fields = ("full_name", "is_vip", "sex", "birth_date")


class ClientDetailSerializer(serializers.ModelSerializer):
    """Детальный вывод по одному клиенту"""

    class Meta:
        model = Client
        fields = '__all__'
