from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from appmain.models import Facturas

# Create your views here.



def index(request):
	return render(request, 'base.html')



# def facturas_list(request):
# 	facturas = Facturas.objects.all()
# 	return render_to_response('base.html', {'facturas': facturas})

def facturas_list(request):
	facturas = Facturas.objects.order_by('-fecha_fact')
	contexto = {'facturas' :facturas}
	return render(request, 'base.html', contexto)