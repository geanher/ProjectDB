from django.contrib import admin
from appmain.views import index
from django.urls import path

urlpatterns = [
    path('', index),

]
