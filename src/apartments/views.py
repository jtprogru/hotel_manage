from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Apartment


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ApartmentView(View):
    """Список номеров"""
    model = Apartment
    queryset = Apartment.objects.all()


class AddApartment(View):
    pass


class ClientView(View):
    pass


class PassportView(View):
    pass
