from productos.views import productos, producto_view
from django.urls import path

app_name = 'productos'
urlpatterns = [
    path('', productos, name='productos'),
    path('nuevo', producto_view, name="productos_crear"),

]


