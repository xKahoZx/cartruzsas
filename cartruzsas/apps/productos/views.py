from django.shortcuts import render_to_response
from django.template import RequestContext
from cartruzsas.apps.productos.forms import *
from cartruzsas.apps.productos.models import *
from cartruzsas.apps.home.forms import *
from cartruzsas.apps.home.models import *
from django.http import HttpResponseRedirect

def add_product_view(request):
	info = "iniciando"
	
	if request.method=="POST":
		formulario = add_product_form(request.POST, request.FILES) 
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.descrip_aux = add.descripcion[0:155]
			add.save()
			if add.categoria == "Accesorio":
				return HttpResponseRedirect ('/accesorios/page/1')
			else:
				return HttpResponseRedirect ('/productos/page/1')
				
	else:
		formulario = add_product_form()
	ctx = {'form':formulario,'informacion': info}
	return render_to_response('productos/add_product.html',ctx, context_instance = RequestContext(request))

def edit_productos_view(request, id_prodc):
	producto = Producto.objects.get(pk = id_prodc)
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES,instance = producto)
		if formulario.is_valid():
			edit = formulario.save(commit = False)
			edit.descrip_aux = edit.descripcion[0:155]
			edit.save()
			if producto.categoria == "Producto":
				return HttpResponseRedirect('/productos/page/1')
			else:
				return HttpResponseRedirect('/accesorios/page/1')
	else:
		formulario = add_product_form(instance = producto)
	ctx = {'form':formulario}
	return render_to_response('productos/edit_productos.html', ctx , context_instance = RequestContext(request))

def add_sabias_view(request):
	info = "iniciando"	
	if request.method=="POST":
		formulario = add_sabias_form(request.POST, request.FILES) 
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.descrip_aux = add.descripcion[0:155]
			add.save()			
			return HttpResponseRedirect ('/sabias/page/1')
	else:
		formulario = add_sabias_form()
	ctx = {'form':formulario,'informacion': info}
	return render_to_response('productos/add_sabias.html',ctx, context_instance = RequestContext(request))

def edit_sabias_view(request, id_item):
	item = Sabias.objects.get(pk = id_item)
	if request.method == "POST":
		formulario = add_sabias_form(request.POST, request.FILES,instance = item)
		if formulario.is_valid():
			edit = formulario.save(commit = False)
			edit.descrip_aux = edit.descripcion[0:155]
			edit.save()
			return HttpResponseRedirect('/sabias/page/1')
	else:
		formulario = add_sabias_form(instance = item)
	ctx = {'form':formulario}
	return render_to_response('productos/edit_sabias.html', ctx , context_instance = RequestContext(request))