from rest_framework import serializers

from .models import Apartment


class ApartmentListSerializer(serializers.ModelSerializer):
    """Список номеров"""

    class Meta:
        model = Apartment
        fields = ("name", "status", "day_price", "night_price", "apartment_type", "description")


class ApartmentDetailSerializer(serializers.ModelSerializer):
    """Список номеров"""

    class Meta:
        model = Apartment
        fields = '__all__'
