from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from train.models import Trains


def home(request):
	trains =Trains.objects.all()
	return render(request, "eticket/home.html",{'trains':trains})



# Create your views here.
