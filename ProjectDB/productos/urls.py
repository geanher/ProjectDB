from productos.views import productos, producto_view, productos_list, producto_edit, producto_delete
from django.urls import path
from django.contrib.auth.decorators import login_required


app_name = 'productos'
urlpatterns = [
    path('', login_required(productos), name='productos'),
    path('nuevo', login_required(producto_view), name="productos_crear"),
    path('listar', login_required(productos_list), name='producto_listar'),
    path('editar/<int:codigo>/' , login_required(producto_edit), name='producto_editar'),
    path('eliminar/<int:codigo>/' , login_required(producto_delete), name='producto_eliminar'),


]


