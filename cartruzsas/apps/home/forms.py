from django import forms
from cartruzsas.apps.home.models import *

class contacto_form(forms.Form):

	nombre 		= forms.CharField (widget  = forms.TextInput())
	correo		= forms.EmailField(widget  = forms.TextInput())
	asunto		= forms.CharField (widget  = forms.TextInput())
	descripcion	= forms.CharField (widget  = forms.Textarea())


class valores_form(forms.ModelForm):
	class Meta:
		model 	= Valores

class Login_form(forms.Form):
	usuario		= forms.CharField(widget = forms.TextInput())
	clave		= forms.CharField(widget = forms.PasswordInput(render_value = True))