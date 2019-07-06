from django.contrib import admin
from appmain.views import index
from django.urls import path

from django.contrib.auth.decorators import login_required


app_name='index'
urlpatterns = [
    path('/', login_required(index), name='index'),

]





