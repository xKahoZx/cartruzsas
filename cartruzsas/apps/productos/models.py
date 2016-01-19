from django.db import models

# Create your models here.

class Producto(models.Model):

	categorias = (
			(u'Accesorio',u'Accesorio'),
			(u'Producto',u'Producto'),
			
		)

	def url(self,filename):
		ruta = "MultimediaData/Producto/%s%s"%(self.nombre, str(filename))
		return ruta


	nombre		= models.CharField(max_length = 100 )
	categoria 	= models.CharField(max_length=50,choices = categorias, default = "Accesorio")
	descripcion	= models.TextField(max_length = 1000)
	descrip_aux	= models.CharField(max_length = 155)
	imagen		= models.ImageField(upload_to = url)
	imagen2		= models.ImageField(upload_to = url)
	imagen3		= models.ImageField(upload_to = url)
	precio 		= models.IntegerField()
	estado		= models.BooleanField(default = True)

	def __unicode__(self):
		return self.nombre