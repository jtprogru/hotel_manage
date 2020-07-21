from django.contrib import admin

from .models import Apartment


class ApartmentAdmin(admin.ModelAdmin):
    """Номера"""
    list_display = ("name", "status", "day_price", "night_price", "apartment_type", "floor", "description")
    list_filter = ("status", "apartment_type")
    search_fields = ("status", "apartment_type")
    inlines = ['ClientInline']
    fieldsets = (
        (None, {
            "fields": ("floor", ("name", "status"))
        }),
        (None, {
            "fields": (("day_price", "night_price"),)
        }),
        (None, {
            "fields": (("apartment_type", "description"),)
        }),
    )


admin.site.register(Apartment)

