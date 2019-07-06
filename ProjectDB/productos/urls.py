from productos.views import productos, producto_view, productos_list
from django.urls import path
from django.contrib.auth.decorators import login_required


app_name = 'productos'
urlpatterns = [
    path('', login_required(productos), name='productos'),
    path('nuevo', login_required(producto_view), name="productos_crear"),
    path('listar', login_required(productos_list), name='producto_listar'),


]


