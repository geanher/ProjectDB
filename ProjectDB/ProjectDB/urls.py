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


