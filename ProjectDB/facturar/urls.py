from django.contrib import admin
from facturar.views import facturar
from django.urls import path

urlpatterns = [
    path('', facturar),

]