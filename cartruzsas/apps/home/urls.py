from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cartruzsas.apps.home.views',

	url(r'^$', 'inicio_view', name = 'vista_inicio'),
	url(r'^nosotros$', 'sobre_nosotros_view', name = 'vista_sobre_nosotros'),
	url(r'^login/$', 'login_view', name = 'vista_login'),
	url(r'^logout/$', 'logout_view', name = 'vista_logout'),
	url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),	
	url(r'^edit/valores/(?P<id_valo>.*)/$', 'edit_valores_view' , name = 'vista_editar_valores'),
	url(r'^productos/page/(?P<pagina>.*)/$', 'productos_view' , name = 'vista_productos'),
	url(r'^sabias/page/(?P<pagina>.*)/$', 'sabias_view' , name = 'vista_sabias'),
	url(r'^accesorios/page/(?P<pagina>.*)/$', 'accesorios_view' , name = 'vista_accesorios'),
	url(r'^listar/inactivos/(?P<opcion>.*)/$', 'listar_inactivos_view' , name = 'vista_inactivos'),
	#url(r'^activar/items/(?P<opcion>.*)/$', 'activar_items_view' , name = 'activar_items'),
	url(r"^activar/items/(?P<id_item>[^/]+)/(?P<opcion>[^/]+)/$", 'activar_items_view' , name = 'activar_items'),
)