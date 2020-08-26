from django.urls import path

from . import views


urlpatterns = [
    path("client/", views.ClientListView.as_view()),
    path("client/<int:pk>/", views.ClientDetailView.as_view()),
]
