from django.contrib import admin
from .models import Client

admin.site.register(Client)

# class ClientInline(admin.StackedInline):
#     model = Client
#     extra = 1


# class PassportInline(admin.StackedInline):
#     model = Passport
#     extra = 1


# class ClientAdmin(ClientInline):
#     """Клиенты"""
#     list_display = ("second_name", "first_name", "middle_name", "status", "is_vip")
#     list_filter = ("status", "is_vip")
#     fieldsets = (
#         (None, {
#             "fields": (("second_name", "first_name", "middle_name"),)
#         }),
#         (None, {
#             "fields": (("status", "is_vip"),)
#         }),
#     )
