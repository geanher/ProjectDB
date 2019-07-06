from personas.views import personas, persona_view, persona_list, persona_edit, persona_delete
from django.urls import path


app_name = 'personas'
urlpatterns = [
    path('', personas, name='personas'),
    path('nuevo', persona_view, name='personas_crear'),
    path('listar', persona_list, name='persona_listar'),
    path('editar/<int:ci_persona>/' , persona_edit, name='persona_editar'),
    path('eliminar/<int:ci_persona>/' , persona_delete, name='persona_eliminar'),
]