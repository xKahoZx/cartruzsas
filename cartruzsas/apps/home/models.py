from django.db import models


#esta tabla guardara la mision, vision y quienes somos de la empresa
class Valores(models.Model):
	mision		= models.TextField(max_length = 1000)
	vision		= models.TextField(max_length = 1000)
	somos		= models.TextField(max_length = 1000)

