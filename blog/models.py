from __future__ import unicode_literals   
from django.db import models 


class GeeksModel(models.Model): 

	title = models.TextField() 
	description = models.TextField() 
  
	def __str__(self): 
		return self.title 

class AuthUser(models.Model):

	username = models.CharField(unique=True, max_length=20)
	email = models.EmailField(unique=True, max_length=50)
	password = models.CharField(unique=False, max_length=20)

	class Meta: 
		managed = False
		db_table = "auth_user"