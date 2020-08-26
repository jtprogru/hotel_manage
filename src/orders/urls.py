from django.urls import path

from . import views


urlpatterns = [
    path("order/", views.OrderListView.as_view()),
    path("order/<int:pk>/", views.OrderDetailView.as_view()),
]
