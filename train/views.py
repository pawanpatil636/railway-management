from django.shortcuts import render, redirect

from .models import Trains


def search_train(request):	
	train = Trains.objects.all()
	for train in Trains.objects.all():
		for station in train.station.all():
			print(station)

	# station = train.stations_set.all()
	# source = Trains.objects.get(pk=request.POST['source'])
 #    dest = Trains.objects.get(pk=request.POST['destination'])

	return render(request,'trains/trains_list.html',{'train':train})
	

# Create your views here.
