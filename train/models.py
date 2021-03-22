from django.db import models


class Stations(models.Model):
	stationname = models.CharField(max_length=200)
	stationcode = models.CharField(max_length=200)
	stationcity = models.CharField(max_length=200)
	prevstation = models.CharField(max_length=200)
	nextstation = models.CharField(max_length=200)


	def __str__(self):
		return str(self.stationname)


class Trains(models.Model):
	trainname = models.CharField(max_length=200)
	trainnumber = models.IntegerField()
	station = models.ManyToManyField(Stations)
	source = models.ForeignKey(Stations,on_delete=models.CASCADE,related_name="source")
	destination = models.ForeignKey(Stations,on_delete=models.CASCADE,related_name="destination")
	arrivaltime = models.CharField(max_length=100)
	departuretime = models.CharField(max_length=100)
	# arrivaldate = models.DateField()
	# departuredate = models.DateField()
	runningdays = models.CharField(max_length=50)
	duration = models.IntegerField()
	trainclass = models.CharField(max_length=50)
	birth = models.CharField(max_length=50)
	availableseats = models.IntegerField()

	def __str__(self):
		return str(self.trainname)