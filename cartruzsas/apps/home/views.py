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
from django.core.paginator import Paginator, EmptyPage, InvalidPage

#Vista inicio
def inicio_view(request):	
	
	formulario = contacto_form()
	if request.method == "POST":
		envio_mail(formulario)
	ctx = {'formu': formulario}

	return render_to_response('home/inicio.html', ctx, context_instance = RequestContext(request))

#Bloque sobre nosotros
def sobre_nosotros_view(request):
	valores = Valores.objects.all()
	formulario = contacto_form()
	if request.method == "POST":
		envio_mail(formulario)
	ctx = {'val':valores, 'formu': formulario}

	return render_to_response('home/nosotros.html', ctx, context_instance = RequestContext(request))

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
#fin bloque sobre nosotros

#bloque lista de productos - accesorios -sabias que...
#vista listar productos
def productos_view(request, pagina):	
	lista_product = Producto.objects.filter(categoria = "Producto", estado = "Activo").order_by('nombre')
	paginator = Paginator(lista_product, 4)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage, InvalidPage):
		productos = paginator.page(paginator.num_pages)

	formulario = contacto_form()
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			envio_mail(formulario)

	ctx = {'product': productos, 'formu':formulario}
	return render_to_response ('home/productos.html', ctx, context_instance = RequestContext(request))
#vista listar accesorios
def accesorios_view(request, pagina):	
	lista_product = Producto.objects.filter(categoria = "Accesorio", estado = "Activo").order_by('nombre')
	paginator = Paginator(lista_product, 4)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage, InvalidPage):
		productos = paginator.page(paginator.num_pages)

	formulario = contacto_form()
	if request.method == "POST":		
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			envio_mail(formulario)
	ctx = {'product': productos, 'formu':formulario}
	return render_to_response ('home/accesorios.html', ctx, context_instance = RequestContext(request))

#vista sabias que...
def sabias_view(request, pagina):	
	lista = Sabias.objects.filter(estado = "Activo").order_by('titulo')
	paginator = Paginator(lista, 4)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		items = paginator.page(page)
	except (EmptyPage, InvalidPage):
		items = paginator.page(paginator.num_pages)

	formulario = contacto_form()
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			envio_mail(formulario)

	ctx = {'lista': items, 'formu':formulario}
	return render_to_response ('home/sabias.html', ctx, context_instance = RequestContext(request))

#fin bloque lista de productos - accesorios - sabias que

#vista listar productos - accesorios - sabias que inactivos
def listar_inactivos_view(request, opcion):
	items = {}
	if opcion == "productos":
		items = Producto.objects.filter(estado = "Inactivo", categoria = "Producto")
	if opcion == "accesorios":
		items = Producto.objects.filter(estado = "Inactivo", categoria = "Accesorio")
	if opcion == "sabias que":
		items = Sabias.objects.filter(estado = "Inactivo")

	ctx = {'items': items, 'opcion' : opcion}
	return render_to_response('home/lista_inactivos.html', ctx, context_instance = RequestContext(request))
#fin vista
#vista activar productos -accesorios - sabias que inactivos
def activar_items_view(request, id_item , opcion):
	item = {}
	ctx = {'opcion': opcion	}
	if opcion == "productos" or opcion == "accesorios":
		item = Producto.objects.get(id = id_item)
		item.estado = "Activo"	
		item.save()	
		if opcion == "accesorios":
			return HttpResponseRedirect('/listar/inactivos/accesorios', ctx ) 
		else:
			return HttpResponseRedirect('/listar/inactivos/productos', ctx ) 
	else:
		item = Sabias.objects.get(id = id_item)
		item.estado = "Activo"	
		item.save()	
		return HttpResponseRedirect('/listar/inactivos/sabias que', ctx ) 
#fin vista
#vista contacanos
def contacto_view(request):
	formulario = contacto_form()
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			envio_mail(formulario)
		
	ctx = {'form':formulario}
	
	return render_to_response('home/contacto.html', ctx, context_instance = RequestContext(request))

#funcion que cargan las otras vista para el envio de correos al gmail
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

#bloque login-logout
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
#fin bloque
