from django.shortcuts import render_to_response
from django.template import RequestContext
from cartruzsas.apps.productos.forms import *
from cartruzsas.apps.productos.models import *
from django.http import HttpResponseRedirect

def add_product_view(request):
	info = "iniciando"
	if request.method=="POST":
		formulario = add_product_form(request.POST, request.FILES) 
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect ('/inicio')
	else:
		formulario = add_product_form()
	ctx = {'form':formulario,'informacion': info}
	return render_to_response('productos/add_product.html',ctx, context_instance = RequestContext(request))
