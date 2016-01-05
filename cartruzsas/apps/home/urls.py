from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cartruzsas.apps.home.views',

	url(r'^inicio/$', 'inicio_view', name = 'vista_inicio'),
	url(r'^edit/valores/(?P<id_valo>.*)/$', 'edit_valores_view' , name = 'vista_editar_valores'),
)