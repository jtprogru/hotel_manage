from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class ApartmentsConfig(AppConfig):
    name = 'apartments'


class HotelAdminConfig(AdminConfig):
    default_site = 'apartments.admin.ApartmentsAdminSite'
