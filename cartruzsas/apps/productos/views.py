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


def add_slider_view(request):
	info = "iniciando"	
	if request.method=="POST":
		formulario = add_slider_form(request.POST, request.FILES) 
		if formulario.is_valid():
			add = formulario.save(commit = False)			
			add.save()
			return HttpResponseRedirect ('/slider')				
	else:
		formulario = add_slider_form()
	ctx = {'form':formulario,'informacion': info}
	return render_to_response('home/add_slider.html',ctx, context_instance = RequestContext(request))

def edit_slider_view(request, id_item):
	item = Slider.objects.get(pk = id_item)
	if request.method == "POST":
		formulario = add_slider_form(request.POST, request.FILES,instance = item)
		if formulario.is_valid():
			edit = formulario.save(commit = False)
			edit.save()
			
			return HttpResponseRedirect('/slider')
	else:
		formulario = add_slider_form(instance = item)
	ctx = {'form':formulario}
	return render_to_response('productos/edit_slider.html', ctx , context_instance = RequestContext(request))


def edit_labor_social(request):
	item = Labor_Social.objects.get(pk = 1)	
	imagenes = Imagen_Labor_Social.objects.all()
	if request.method == "POST":
		formulario = edit_labor_social_form(request.POST, request.FILES,instance = item)
		if formulario.is_valid():
			edit = formulario.save(commit = False)
			edit.save()			
			return HttpResponseRedirect('/')
	else:
		formulario = edit_labor_social_form(instance = item)
	ctx = {'form':formulario, 'img': imagenes}
	return render_to_response('productos/edit_labor_social.html', ctx , context_instance = RequestContext(request))

def edit_imagen_Labor_Social(request, id_img):
	img = Imagen_Labor_Social.objects.get(pk = id_img)
	if request.method == "POST":
		formulario = edit_labor_imagen_social_form(request.POST, request.FILES,instance = img)
		if formulario.is_valid():
			edit = formulario.save(commit = False)
			edit.save()			
			return HttpResponseRedirect('/edit/labor')
	else:
		formulario = edit_labor_imagen_social_form(instance = img)
	ctx = {'form':formulario}
	return render_to_response('productos/edit_labor_social_img.html', ctx , context_instance = RequestContext(request))








