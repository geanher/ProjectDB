from django.shortcuts import render, redirect
from django.http import HttpResponse
from productos.forms import ProductosForm

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