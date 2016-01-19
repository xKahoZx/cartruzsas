from django.shortcuts import render_to_response
from django.template import RequestContext
from cartruzsas.apps.home.forms import *
from cartruzsas.apps.home.models import *
from cartruzsas.apps.productos.forms import *
from cartruzsas.apps.productos.models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import login, logout, authenticate


def inicio_view(request):	
	valores = Valores.objects.all()
	formulario = contacto_form()
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			envio_mail(formulario)


	ctx = {'val':valores, 'formu': formulario}

	return render_to_response('home/inicio.html', ctx, context_instance = RequestContext(request))


def edit_valores_view(request, id_valo):
	
	valores = Valores.objects.get(pk = id_valo)
	if request.method == "POST":
		formulario = valores_form(request.POST, instance = valores)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/inicio/')
	else:
		formulario = valores_form(instance = valores)
	ctx = {'form':formulario}
	return render_to_response('home/edit_valores.html', ctx , context_instance = RequestContext(request))

def productos_view(request):	
	lista_product = Producto.objects.filter(categoria = "Producto")
	formulario = contacto_form()
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			envio_mail(formulario)
		
	ctx = {'product': lista_product, 'formu':formulario}
	return render_to_response ('home/productos.html', ctx, context_instance = RequestContext(request))

def accesorios_view(request):
		
	lista_product = Producto.objects.filter(categoria = "Accesorio")
	formulario = contacto_form()
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			envio_mail(formulario)
			
	ctx = {'product': lista_product, 'formu':formulario}
	return render_to_response ('home/accesorios.html', ctx, context_instance = RequestContext(request))

def contacto_view(request):
	formulario = contacto_form()
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			envio_mail(formulario)
		
	ctx = {'form':formulario}
	
	return render_to_response('home/contacto.html', ctx, context_instance = RequestContext(request))

def envio_mail(formulario):
	email 		= formulario.cleaned_data=['correo']
	nombre 	 	= formulario.cleaned_data=['nombre']
	asunto  	= formulario.cleaned_data=['asunto']
	descripcion = formulario.cleaned_data=['descripcion']
	to_admin = 'datutalcha3@misena.edu.co'
	html_content = "Informacion recibida de %s <br> ----Mensaje--- <br> %s"%(nombre, asunto)
	msg = EmailMultiAlternatives(asunto, html_content, 'from@server.com', [to_admin])
	msg.attach_alternative(html_content, 'text/html')
	msg.send()

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form()
		ctx = {'form': formulario, 'men': mensaje}
		return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')