from django.shortcuts import render, redirect
from django.http import HttpResponse
from personas.forms import PersonasForm, preguntasForm, detallebancoForm, detallebancoFormSet
from appmain.models import Clientes, DetBancos, Preguntas
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory


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

class CreateViewDetails(CreateView):
    template_name = 'bancos/creardetalles.html'
    model = DetBancos
    form_class = detallebancoForm 

    def get_success_url(self):
        return reverse('DetBanca-created')#ojooooo


    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(CreateViewDetails, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = detallebancoForm(self.request.POST)
            ctx['inlines'] = detallebancoFormSet(self.request.POST)
        else:
            ctx['form'] = detallebancoForm
            ctx['inlines'] = detallebancoFormSet()
        return ctx
