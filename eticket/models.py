from django.db import models
from django.contrib.auth.models import User

class PassengerDetail(models.Model):
	user = models.CharField(max_length=30, null=True)
	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30,null=True)
	birth = models.CharField(max_length=30)
	age = models.IntegerField()


	def __str__(self):
		return str (self.birth)

class Address(models.Model):
	address1 = models.CharField(max_length=30)
	address2 = models.CharField(max_length=30)
	city =  models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	pincode = models.IntegerField()
	

	def __str__(self):
		return str(self.city)


		


 

