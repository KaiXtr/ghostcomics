from django.db import models

class User(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	username = models.CharField(max_length=200,blank=True,null=True)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name