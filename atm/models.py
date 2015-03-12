from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=10)
	account = models.PositiveIntegerField()
	password = models.CharField(max_length=9)
	contact = models.CharField(max_length=11)
	city = models.CharField(max_length=20)
	

