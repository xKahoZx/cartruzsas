from django import forms
from cartruzsas.apps.productos.models import *

class add_product_form(forms.ModelForm):
	class Meta:
		model   = Producto
		exclude = ('descrip_aux')

class add_sabias_form(forms.ModelForm):
	class Meta:
		model 	= Sabias
		exclude = ('descrip_aux')

class add_slider_form(forms.ModelForm):
	class Meta:
		model 	= Slider

class edit_labor_social_form(forms.ModelForm):
	class Meta:
		model = Labor_Social
		exclude = ('imagen')

class edit_labor_imagen_social_form(forms.ModelForm):
	class Meta:
		model = Imagen_Labor_Social
