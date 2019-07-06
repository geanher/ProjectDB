from personas.views import personas, persona_view, persona_list
from django.urls import path


app_name = 'personas'
urlpatterns = [
    path('', personas, name='personas'),
    path('nuevo', persona_view, name='personas_crear'),
    path('listar', persona_list, name='persona_listar'),



]