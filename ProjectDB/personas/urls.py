from personas.views import personas, persona_view, persona_list, persona_edit, persona_delete,  CreateViewDetails
from django.urls import path
from django.contrib.auth.decorators import login_required


app_name = 'personas'
urlpatterns = [
    path('', login_required(personas), name='personas'),
    path('nuevo', login_required(persona_view), name='personas_crear'),
    path('listar', login_required(persona_list), name='persona_listar'),
    path('editar/<int:ci_persona>/' , login_required(persona_edit), name='persona_editar'),
    path('eliminar/<int:ci_persona>/' , login_required(persona_delete), name='persona_eliminar'),
    #path('banklist/<int:ci_persona>/' , login_required(persona_banco.as_view()), name='persona_banco'),
    path('banklist/crear/' , login_required(CreateViewDetails.as_view()), name='detallebanc'),

]