from django.contrib import admin
from estadisticas.views import estadisticas
from django.urls import path

urlpatterns = [
    path('', estadisticas),

]