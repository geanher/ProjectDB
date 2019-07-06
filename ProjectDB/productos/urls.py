from productos.views import productos, producto_view, productos_list
from django.urls import path

app_name = 'productos'
urlpatterns = [
    path('', productos, name='productos'),
    path('nuevo', producto_view, name="productos_crear"),
    path('listar', productos_list, name='producto_listar'),


]


