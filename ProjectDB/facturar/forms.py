from django import forms
from appmain.models import Clientes, DetBancos, Preguntas, Facturas, DetFact, Productos
from django.forms import inlineformset_factory, modelformset_factory


class facturaForm(forms.ModelForm):
	class Meta: 
		model=Facturas

		fields = [
			'ci',
			'fecha_fact',

		]
		labels = {
			'ci' : 'CI',
			'fecha_fact' : 'Fecha factura',
			}
		widgets = {
			'ci': forms.Select(attrs={'class':'form-control'}),
			'fecha_fact': forms.DateInput(attrs={'class':'form-control'}),

		}

class ProductosForm(forms.ModelForm):
	class Meta:
		model=Productos

		fields =  [
    		'nombre',
    		'tipo_prod',
    		'precio',
		] 

		labels = {

    		'nombre': 'Nombre  del producto',
    		'tipo_prod': 'tipo de producto',
    		'precio': 'Precio',
		}
		widgets = {

    		'nombre': forms.TextInput(attrs={'class':'form-control'}),
    		'tipo_prod': forms.Select(attrs={'class':'form-control'}),
    		'precio': forms.TextInput(attrs={'class':'form-control'}),
		}

class DetFactForm(forms.ModelForm):
	class meta: 
		model=DetFact

		fields = [
		    'cod_producto',
		    'cantidad',
		    'precio',
		    'detalles',
		]
		labels = {
			'cod_producto': 'codigo del producto',
		    'cantidad':'cantidad del producto',
		    'precio': 'Precio del producto',
		    'detalles':'Detalles del producto',
    	}

		widgets = {
			'cod_producto': forms.TextInput(attrs={'class': 'form-control'}),
		    'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
		    'precio': forms.TextInput(attrs={'class': 'form-control'}),
		    'detalles': forms.TextInput(attrs={'class': 'form-control'}),
    	}


facturaFormSet = inlineformset_factory(Facturas, DetFact, form = DetFactForm, fields = ['cod_producto', 'cantidad', 'precio', 'detalles',], extra=1)