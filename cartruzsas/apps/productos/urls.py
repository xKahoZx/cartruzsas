from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cartruzsas.apps.productos.views',
	url(r'^add/product/$','add_product_view', name = 'vista_agregar_producto'),
	url(r'^edit/product/(?P<id_prodc>.*)/$', 'edit_productos_view' , name = 'vista_editar_productos'),
	
)