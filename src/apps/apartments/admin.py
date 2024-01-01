from django.contrib import admin

from .models import Apartment


class ApartmentAdmin(admin.ModelAdmin):
    """Номера"""
    list_display = ("name", "status", "day_price", "night_price", "apartment_type", "description")
    list_filter = ("status", "apartment_type")
    search_fields = ("status", "apartment_type")
    fieldsets = (
        ("Номер", {
            "fields": (("name", "status", "apartment_type"),)
        }),
        ("Стоимость", {
            "fields": (("day_price", "night_price"),)
        }),
        ("Доп. инфа", {
            "fields": (("description",),)
        }),
    )


admin.site.register(Apartment, ApartmentAdmin)

