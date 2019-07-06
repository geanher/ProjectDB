from django.contrib import admin
from appmain.views import index
from django.urls import path

app_name='index'
urlpatterns = [
    path('', index, name='index'),

]





