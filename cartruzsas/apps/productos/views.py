from django.shortcuts import render_to_response
from django.template import RequestContext
from cartruzsas.apps.productos.forms import *
from cartruzsas.apps.productos.models import *
from cartruzsas.apps.home.forms import *
from cartruzsas.apps.home.models import *
from django.http import HttpResponseRedirect

def add_product_view(request):
	info = "iniciando"
	formulario_cont = contacto_form()
	if request.method=="POST":
		formulario = add_product_form(request.POST, request.FILES) 
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			if add.categoria == "Accesorio":
				return HttpResponseRedirect ('/accesorios')
			else:
				return HttpResponseRedirect ('/productos')
				
	else:
		formulario = add_product_form()
	ctx = {'form':formulario,'informacion': info, 'formu':formulario}
	return render_to_response('productos/add_product.html',ctx, context_instance = RequestContext(request))

def edit_productos_view(request, id_prodc):
	formulario_cont = contacto_form()
	producto = Producto.objects.get(pk = id_prodc)
	if request.method == "POST":
		formulario = add_product_form(request.POST, instance = producto)
		if formulario.is_valid():
			formulario.save()
			if producto.categoria == "Producto":
				return HttpResponseRedirect('/productos')
			else:
				return HttpResponseRedirect('/accesorios')
	else:
		formulario = add_product_form(instance = producto)
	ctx = {'form':formulario, 'formu':formulario_cont}
	return render_to_response('productos/edit_productos.html', ctx , context_instance = RequestContext(request))

