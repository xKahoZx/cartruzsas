from django.db import models

# Create your models here.

class Producto(models.Model):

	def url(self):
		ruta = "MultimediaData/Producto/%s%s"%(self.nombre, str(filename))
		return ruta


	nombre		= models.CharField(max_length = 100 )
	descripcion	= models.TextField(max_length = 500)
	imagen		= models.ImageField(upload_to = url, null = True, blank = True)
	#imagen2		= models.ImageField(upload_to = url2, null = True, blank = True)
	precio 		= models.IntegerField()