"""ProjectDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('appmain.urls', namespace='index')),
    path('personas/' , include('personas.urls', namespace='personas')),
    path('facturar/' , include('facturar.urls')),
    path('productos/' , include('productos.urls', namespace='productos')),
    path('estadisticas/' , include('estadisticas.urls')),
    path('usuario/' , include('usuario.urls', namespace='usuario')),
    path('accounts/login/' , auth_views.LoginView.as_view(), name='login'),
    path('logout/' , logout_then_login, name='logout'),


]


