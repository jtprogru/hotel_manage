from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    """Заказы"""
    list_display = ("id", "status", "date_start", "date_end")
    list_filter = ("status", )
    search_fields = ("status", "date_start", "date_end")


admin.site.register(Order, OrderAdmin)
