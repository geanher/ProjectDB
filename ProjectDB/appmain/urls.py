from django.contrib import admin
from appmain.views import index, facturas_list
from django.urls import path

from django.contrib.auth.decorators import login_required


app_name='index'
urlpatterns = [
    path('', login_required(facturas_list), name='index'),

]





