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
