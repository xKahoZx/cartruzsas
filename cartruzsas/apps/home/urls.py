from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cartruzsas.apps.home.views',

	url(r'^$', 'inicio_view', name = 'vista_inicio'),
	url(r'^login/$', 'login_view', name = 'vista_login'),
	url(r'^logout/$', 'logout_view', name = 'vista_logout'),
	url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),	
	url(r'^edit/valores/(?P<id_valo>.*)/$', 'edit_valores_view' , name = 'vista_editar_valores'),
	url(r'^productos/$', 'productos_view' , name = 'vista_productos'),
	url(r'^accesorios/$', 'accesorios_view' , name = 'vista_accesorios'),
)