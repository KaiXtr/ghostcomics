from django.db import models

class Brand(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class Console(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	brand = models.ForeignKey(Brand,on_delete=models.PROTECT,related_name="console_brand")
	year = models.IntegerField(blank=True,null=True)
	
	def __str__(self):
		return self.name