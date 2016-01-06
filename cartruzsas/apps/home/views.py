from django.shortcuts import render_to_response
from django.template import RequestContext
from cartruzsas.apps.home.forms import *
from cartruzsas.apps.home.models import *
from cartruzsas.apps.productos.forms import *
from cartruzsas.apps.productos.models import *
from django.http import HttpResponseRedirect


def inicio_view(request):
	formulario = contacto_form()
	valores = Valores.objects.all()
	ctx = {'val':valores, 'formu':formulario}

	return render_to_response('home/inicio.html', ctx, context_instance = RequestContext(request))


def edit_valores_view(request, id_valo):
	formulario_cont = contacto_form()
	valores = Valores.objects.get(pk = id_valo)
	if request.method == "POST":
		formulario = valores_form(request.POST, instance = valores)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/inicio/')
	else:
		formulario = valores_form(instance = valores)
	ctx = {'form':formulario, 'formu':formulario_cont}
	return render_to_response('home/edit_valores.html', ctx , context_instance = RequestContext(request))

def productos_view(request):
	formulario = contacto_form()	
	lista_product = Producto.objects.filter(categoria = "Producto")
	ctx = {'product': lista_product, 'formu':formulario}
	return render_to_response ('home/productos.html', ctx, context_instance = RequestContext(request))

def accesorios_view(request):
	formulario = contacto_form()	
	lista_product = Producto.objects.filter(categoria = "Accesorio")
	ctx = {'product': lista_product, 'formu':formulario}
	return render_to_response ('home/accesorios.html', ctx, context_instance = RequestContext(request))