from django.contrib import admin
from django.urls import path, include
from app.views import EmailFormView

urlpatterns = [
    path("", EmailFormView.as_view(), name="home"),
]