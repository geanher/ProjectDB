from django import forms
from appmain.models import Clientes, DetBancos, Preguntas
from django.forms import inlineformset_factory
from django.forms import modelformset_factory


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


class detallebancoForm(forms.ModelForm):
	class Meta: 
		model = DetBancos

		fields = [
			'ci',
			'idbanco',
			'tipo_cuenta',
			'n_cuenta',
			'n_tarjeta',
			'cod_seg',
			'fecha_vencimiento',
			'usuario_internet',
			'clave_internet',
			'clave_cajero',
			'num_telefono',
			'clave_especial',
		]
		labels = {
			'ci' : 'CI',
			'idbanco' : 'IdBanco',
			'tipo_cuenta': 'Tipo de cuenta',
			'n_cuenta': 'Numero de cuenta',
			'n_tarjeta': 'Numero de Tarjeta',
			'cod_seg': 'Codigo de Seguridad',
			'fecha_vencimiento': 'Fecha de Vencimiento',
			'usuario_internet': 'Usuario por Internet',
			'clave_internet': 'Clave De usuario',
			'clave_cajero': 'clave de cajero',
			'num_telefono': 'telefono asociado',
			'clave_especial':'clave espcial',
			}
		widgets = {
			'ci': forms.Select(attrs={'class':'form-control'}),
			'idbanco': forms.Select(attrs={'class':'form-control'}),
			'tipo_cuenta': forms.TextInput(attrs={'class':'form-control'}),
			'n_cuenta': forms.TextInput(attrs={'class':'form-control'}),
			'n_tarjeta': forms.TextInput(attrs={'class':'form-control'}),
			'cod_seg': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_vencimiento': forms.TextInput(attrs={'class':'form-control'}),
			'usuario_internet': forms.TextInput(attrs={'class':'form-control'}),
			'clave_internet': forms.TextInput(attrs={'class':'form-control'}),
			'clave_cajero': forms.TextInput(attrs={'class':'form-control'}),
			'num_telefono': forms.TextInput(attrs={'class':'form-control'}),
			'clave_especial': forms.TextInput(attrs={'class':'form-control'}),

		}

class preguntasForm(forms.ModelForm):
	class Meta: 
		model = Preguntas

		fields = [
			'n_cuenta',
		    'pregunta',	
		    'respuesta',
		]
		labels = {
			'pregunta': 'Pregunta',
		    'respuesta': 'Respuesta',
    	}

		widgets = {
			'pregunta': forms.TextInput(attrs={'class': 'form-control'}),
		    'respuesta': forms.TextInput(attrs={'class': 'form-control'}),
    	}

detallebancoFormSet = inlineformset_factory(DetBancos, Preguntas, form=preguntasForm, fields=('pregunta' , 'respuesta'), extra=1)