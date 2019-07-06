from django.urls import path
from usuario.views import RegistroUsuario

app_name ='usuario'

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name='registrar')


]
