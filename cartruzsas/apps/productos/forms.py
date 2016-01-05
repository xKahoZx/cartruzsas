from django import forms
from cartruzsas.apps.productos.models import *

class add_product_form(forms.ModelForm):
	class Meta:
		model   = Producto
