from django.urls import path

from . import views


urlpatterns = [
    path("apartment/", views.ApartmentListView.as_view()),
    path("apartment/<int:pk>/", views.ApartmentDetailView.as_view()),
    path("apartment/create/", views.ApartmentCreateView.as_view()),
]
