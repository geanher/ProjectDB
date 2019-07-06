from django.shortcuts import render, redirect
from django.http import HttpResponse
from personas.forms import PersonasForm
from appmain.models import Clientes

# Create your views here.


def personas(request):
	return render(request, 'personas/personas.html')



def persona_view(request):
	if request.method == 'POST':
		form = PersonasForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('personas:personas')
	else:
		form = PersonasForm()
	return render(request, 'personas/personas_form.html', {'form': form})


def persona_list(request):
	persona = Clientes.objects.all()
	contexto = {'personas' :persona}
	return render(request, 'personas/personas_list.html', contexto)
