from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("123", views.index123, name="index123"),
]
