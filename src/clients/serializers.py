from rest_framework import serializers

from .models import Client


class ClientListSerializer(serializers.ModelSerializer):
    """Список клиентов"""

    class Meta:
        model = Client
        fields = ("full_name", "is_vip", "sex", "birth_date")


class ClientDetailSerializer(serializers.ModelSerializer):
    """Подробный вывод по одному клиенту"""

    class Meta:
        model = Client
        fields = ("full_name", "is_vip", "passport_sn", "police_department", "police_department_id", "date_issue",
                  "sex", "birth_date", "birth_place", "registration")
