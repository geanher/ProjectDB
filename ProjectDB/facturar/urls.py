from django.contrib import admin
#from facturar.views import facturar
from facturar.views import CreateViewDetails
from django.urls import path
from django.contrib.auth.decorators import *

app_name= 'facturar'
urlpatterns = [
    path('', login_required(CreateViewDetails.as_view()), name='facturar'),


]