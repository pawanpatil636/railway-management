from django.db import models
from django.contrib.auth.models import User 

	

GENDER_CHOICES=(
   ('male','male'), 
   ('female','female'),
   ('others','others'),
)
class Account(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	age = models.IntegerField()
	phone = models.IntegerField()
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES) 
	dob = models.DateField()
	aadharproof = models.ImageField(upload_to="images")
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	maritalstatus = models.CharField(max_length=30)
	password = models.CharField(max_length=20)



	def __str__(self):
		return str(self.user)


# Create your models here.
