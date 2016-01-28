from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cartruzsas.apps.productos.views',
	url(r'^add/product/$','add_product_view', name = 'vista_agregar_producto'),
	url(r'^add/sabias/$','add_sabias_view', name = 'vista_agregar_sabias'),
	url(r'^edit/product/(?P<id_prodc>.*)/$', 'edit_productos_view' , name = 'vista_editar_productos'),
	url(r'^edit/sabias/(?P<id_item>.*)/$', 'edit_sabias_view' , name = 'vista_editar_sabias'),
	
)