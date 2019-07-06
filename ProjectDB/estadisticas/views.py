from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def estadisticas(request):
	return render(request, 'estadisticas/estadisticas.html')