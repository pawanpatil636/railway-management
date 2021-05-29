from django.shortcuts import render, redirect

from .models import Trains,Stations


def search_train(request):
	train = Trains.objects.get(id=3)
	print(train)
	station = Stations.objects.all()

	lis = []
	for st in train.station.all():
		lis.append(st)

	
	return render(request,'trains/trains_list.html',{'train':train,'station':station})
	

# Create your views here.
