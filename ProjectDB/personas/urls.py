from personas.views import personas, persona_view
from django.urls import path

app_name = 'personas'
urlpatterns = [
    path('', personas, name='personas'),
    path('nuevo', persona_view, name='personas_crear'),


]