from django.shortcuts import render
from django.http import HttpResponse
from facturar.forms import facturaForm
from django.views.generic import ListView, CreateView
from appmain.models import Facturas, DetFact
from django.forms import formset_factory
from facturar.forms import facturaFormSet




class CreateViewDetails(CreateView):
    template_name = 'facturar/facturar.html'
    model = Facturas
    form_class = facturaForm 


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
            ctx['form'] = facturasForm(self.request.POST)
            ctx['inlines'] = facturaFormSet(self.request.POST)
        else:
            ctx['form'] = Facturas()
            ctx['inlines'] = facturaFormSet()
        return ctx