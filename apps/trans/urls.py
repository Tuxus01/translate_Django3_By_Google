
from django.contrib import admin
from .views import traductor,Traductor2
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', traductor),
    #path('post/traduccion/<str:to>/(?P<str:to_text>\w{0,50})/$/<str:from_l>/', Traductor2, name = "Traductor"),
    path('post/traduccion/<str:to>/<str:from_l>/', Traductor2, name = "Traductor"),
]
