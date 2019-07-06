from django.contrib import admin
from productos.views import productos
from django.urls import path

urlpatterns = [
    path('', productos),

]