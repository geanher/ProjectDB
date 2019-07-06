from django import forms
from appmain.models import Productos


class ProductosForm(forms.ModelForm):
	class Meta:
		model = Productos

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