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
	descripcion	= models.TextField(max_length = 500)
	imagen		= models.ImageField(upload_to = url, null = True, blank = True)
	imagen2		= models.ImageField(upload_to = url, null = True, blank = True)
	precio 		= models.IntegerField()
	estado		= models.BooleanField(default = True)