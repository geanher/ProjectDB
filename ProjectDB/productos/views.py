from django.shortcuts import render, redirect
from django.http import HttpResponse
from productos.forms import ProductosForm
from appmain.models import Productos

# Create your views here.


def productos(request):
	return render(request, 'productos/productos.html')



def producto_view(request):
	if request.method == 'POST':
		form = ProductosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('productos:productos')
	else:
		form = ProductosForm()
	return render(request, 'productos/productos_form.html', {'form': form})


def productos_list(request):
	producto = Productos.objects.all()
	contexto = {'productos' :producto}
	return render(request, 'productos/productos_list.html', contexto)