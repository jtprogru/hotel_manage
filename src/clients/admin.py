from django.contrib import admin
from .models import Client, Passport


class ClientInline(admin.StackedInline):
    model = Client
    extra = 1


class PassportInline(admin.StackedInline):
    model = Passport
    extra = 1


class ClientAdmin(ClientInline):
    """Клиенты"""
    list_display = ("second_name", "first_name", "middle_name", "status", "is_vip")
    list_filter = ("status", "is_vip")
    inlines = ['PassportInline']
    fieldsets = (
        (None, {
            "fields": (("second_name", "first_name", "middle_name"),)
        }),
        (None, {
            "fields": (("status", "is_vip"),)
        }),
    )


class PassportAdmin(PassportInline):
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


admin.site.register(Client)
admin.site.register(Passport)
