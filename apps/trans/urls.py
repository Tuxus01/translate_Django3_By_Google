
from django.contrib import admin
from .views import traductor
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', traductor),
]
