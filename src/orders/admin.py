from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    """Заказы"""
    list_display = ("status", "type", "date_start", "date_end")
    list_filter = ("status", "type", "date_start", "date_end")
    search_fields = ("status", "type", "date_start", "date_end")


admin.site.register(Order)
