from django.db import models

class Genre(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class Company(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class Gibi(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	genre = models.ForeignKey(Genre,on_delete=models.PROTECT,related_name="gibi_genre")
	company = models.ForeignKey(Company,on_delete=models.PROTECT,related_name="gibi_company")
	volume = models.IntegerField(blank=True,null=True)
	rate = models.IntegerField(blank=True,null=True)
	price = models.IntegerField(blank=True,null=True)
	year = models.IntegerField(blank=True,null=True)
	
	def __str__(self):
		return self.name