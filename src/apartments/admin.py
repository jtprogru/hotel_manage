from django.contrib import admin

from .models import Apartment, Client, Passport


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    """Номера"""
    list_display = ("name", "status", "day_price", "night_price", "apartment_type", "floor", "description")
    list_filter = ("status", "apartment_type")
    search_fields = ("status", "apartment_type")
    inlines = [Client, ]
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


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Клиенты"""
    list_display = ("second_name", "first_name", "middle_name", "status", "is_vip")
    list_filter = ("status", "is_vip")
    inlines = [Passport, ]
    fieldsets = (
        (None, {
            "fields": (("second_name", "first_name", "middle_name"),)
        }),
        (None, {
            "fields": (("status", "is_vip"),)
        }),
    )


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    """Паспорта"""
    list_display = ("serial", "number", "police_department", "police_department_id",
                    "date_issue", "sex", "birth_date", "birth_place", "registration")
    fieldsets = (
        (None, {
            "fields": (("serial", "number"),)
        }),
        (None, {
            "fields": (("police_department",),)
        }),
        (None, {
            "fields": (("date_issue", "police_department_id"),)
        }),
        (None, {
            "fields": (("sex", "birth_date"), "birth_place")
        }),
        (None, {
            "fields": (("registration",),)
        }),
    )
