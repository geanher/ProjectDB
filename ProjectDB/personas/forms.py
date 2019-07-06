from django import forms
from appmain.models import Clientes


class PersonasForm(forms.ModelForm):
	class Meta:
		model = Clientes

		fields =  [
			'ci',
    		'nombre',
    		'apellido',
		    'telefono',
		    'direccion',
		    'fecha_nac',
		    'genero',
		] 

		labels = {
			'ci': 'CI',
    		'nombre': 'Nombre',
    		'apellido ': 'Apellidos',
		    'telefono': 'telefono',
		    'direccion': 'direccion',
		    'fecha_nac': 'fecha de nacimiento',
		    'genero': 'genero',

		}
		widgets = {
			'ci': forms.TextInput(attrs={'class':'form-control'}),
    		'nombre ': forms.TextInput(attrs={'class':'form-control'}),
    		'apellido ': forms.TextInput(attrs={'class':'form-control'}),
		    'telefono': forms.TextInput(attrs={'class':'form-control'}),
		    'direccion': forms.TextInput(attrs={'class':'form-control'}),
		    'fecha_nac': forms.TextInput(attrs={'class':'form-control'}),
		    'genero': forms.TextInput(attrs={'class':'form-control'}),	
		}