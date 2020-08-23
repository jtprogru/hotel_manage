from django.urls import path
from . import views

urlpatterns = [
    path("", views.ApartmentView.as_view()),
    path("<int:pk>/", views.AddApartment.as_view(), name="add_apartment"),
]
