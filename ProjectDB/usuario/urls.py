from django.urls import path
from usuario.views import RegistroUsuario
from django.contrib.auth.decorators import login_required


app_name ='usuario'

urlpatterns = [
    path('registrar', login_required(RegistroUsuario.as_view()), name='registrar')


]
