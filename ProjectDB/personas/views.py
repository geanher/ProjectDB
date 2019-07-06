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



def persona_edit(request, ci_persona):
	persona = Clientes.objects.get(ci=ci_persona)
	if request.method == 'GET':
		form = PersonasForm(instance=persona)
	else:
		form = PersonasForm(request.POST, instance=persona)
		if form.is_valid():
			form.save()
		return redirect('personas:persona_listar')
	return render(request, 'personas/personas_form.html', {'form':form})


def persona_delete(request, ci_persona):
	persona = Clientes.objects.get(ci = ci_persona)
	if request.method == 'POST' :
		persona.delete()
		return redirect('personas:persona_listar')
	return render(request, 'personas/persona_delete.html', {'persona' :persona})
	