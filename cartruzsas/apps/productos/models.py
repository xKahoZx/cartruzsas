from django.db import models

# Create your models here.

estados = (
		(u'Activo',u'Activo'),
		(u'Inactivo',u'Inactivo'),
	)

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
	imagen_1	= models.ImageField(upload_to = url)
	imagen_2	= models.ImageField(upload_to = url)
	imagen_3	= models.ImageField(upload_to = url)
	precio 		= models.IntegerField()
	estado		= models.CharField(max_length= 15,choices = estados, default = "Activo")

	def __unicode__(self):
		return self.nombre

class Sabias(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Sabias/%s%s"%(self.titulo, str(filename))
		return ruta

	titulo		= models.CharField(max_length = 100)
	descripcion	= models.TextField(max_length = 10000)
	descrip_aux	= models.TextField(max_length = 150)
	imagen_1	= models.ImageField(upload_to = url)
	imagen_2	= models.ImageField(upload_to = url)
	imagen_3	= models.ImageField(upload_to = url)
	estado		= models.CharField(max_length= 15,choices = estados, default = "Activo")

class Slider(models.Model):
	
	estados = (
		(u'Activo',u'Activo'),
		(u'Inactivo',u'Inactivo'),
	)

	def url(self,filename):
		ruta = "MultimediaData/Slider/%s.jpg"%(self.titulo)
		return ruta

	titulo		= models.CharField(max_length = 20)
	texto		= models.CharField(max_length = 50)
	imagen		= models.ImageField(upload_to = url)
	estado		= models.CharField(max_length = 20, choices = estados, default = "Activo")

	def __unicode__(self):
		return self.titulo


class Imagen_Labor_Social(models.Model):
	
	def  url(self,filename):
		ruta = "MultimediaData/Labor_Social/%s.jpg"%(self.nombre)
		return ruta
	nombre 		= models.CharField(max_length = 100, unique = True)
	imagen 		= models.ImageField(upload_to = url)

	def __unicode__(self):
		return self.nombre

class Labor_Social(models.Model):
	
	encabezado		= models.CharField(max_length = 200)
	imagen 			= models.ManyToManyField(Imagen_Labor_Social)

	def __unicode__(self):
		return self.encabezado










