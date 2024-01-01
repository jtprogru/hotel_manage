from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    """Клиенты"""
    list_display = ("full_name", "is_vip", "sex", "birth_date")
    list_filter = ("is_vip", "sex")
    fieldsets = (
        ("ФИО", {
            "fields": (("second_name", "first_name", "middle_name"),)
        }),
        ("Статус/Пол/ДР", {
            "fields": (("is_vip", "sex", "birth_date"),)
        }),
        ("Паспорт", {
            "fields": (("serial", "number", "date_issue"),
                       ("police_department_id", "police_department"),
                       ("birth_place", "registration"),)
        }),
    )


admin.site.register(Client, ClientAdmin)
