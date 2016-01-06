from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cartruzsas.apps.home.views',

	url(r'^$', 'inicio_view', name = 'vista_inicio'),
	url(r'^edit/valores/(?P<id_valo>.*)/$', 'edit_valores_view' , name = 'vista_editar_valores'),
	url(r'^productos/$', 'productos_view' , name = 'vista_productos'),
	url(r'^accesorios/$', 'accesorios_view' , name = 'vista_accesorios'),
)