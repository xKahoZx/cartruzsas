from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cartruzsas.apps.productos.views',
	url(r'^add/product/$','add_product_view', name = 'vista_agregar_producto'),
	url(r'^add/sabias/$','add_sabias_view', name = 'vista_agregar_sabias'),
	url(r'^add/slider/$','add_slider_view', name = 'vista_agregar_slider'),
	url(r'^edit/product/(?P<id_prodc>.*)/$', 'edit_productos_view' , name = 'vista_editar_productos'),
	url(r'^edit/sabias/(?P<id_item>.*)/$', 'edit_sabias_view' , name = 'vista_editar_sabias'),
	url(r'^edit/slider/(?P<id_item>.*)/$', 'edit_slider_view' , name = 'vista_editar_slider'),
	url(r'^edit/labor/$', 'edit_labor_social' , name = 'vista_editar_labor'),
	url(r'^edit/img/(?P<id_img>.*)/$', 'edit_imagen_Labor_Social' , name = 'vista_editar_img_labor'),
	
)