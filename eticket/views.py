from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from train.models import Trains ,Stations
from .forms import SearchForm
from train.views import search_train
from .models import PassengerDetail
from account.models import Account


def home(request):
	trains = Trains.objects.all()
	# if request.method == "POST":

	# 	return redirect ('/eticket/search-result/')
	return render(request, "eticket/home.html",{'trains':trains})

def srch(request):
	trains = Trains.objects.all()
	station = Stations.objects.all()
	# form = SearchForm(request.POST)
	# if request.method == "POST":
	# 	if form.is_valid():
	# 		data = form.cleaned_data
	# 		src = data['src']
	# 		dest = data['dest']
	a = request.GET.get('source')
	b = request.GET.get('destination')
	# form = SearchForm()
	return render(request, "eticket/search_result.html",{'station':station,'trains':trains,'a':a,'b':b})
	
def passenger_details(request):
	if request.method == "POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		berth = request.POST['berth']
		age = request.POST['age']
		print(last_name)

		user = PassengerDetail(user=request.user, first_name=first_name,last_name=last_name,birth=berth,age=age)
		user.save()

	return render(request, "eticket/passenger_details.html")


def user_account(request):
	details = Account.objects.all()

	return render(request, "eticket/user_account.html",{'details':details})



# def search_view(request):
# 	trains = Trains.objects.all()

	

    # if src and dest:
    #     match = Trains.objects.filter(user__is_active=True, variety__icontains=srch)
    #     print(match)
 #        if match:
 #            no_of_item = match.count()
 #            messages.success(self.request, str(no_of_item) + " results found for " + srch)
 #        else: 
 #            messages.warning(self.request, 'No result found for ' + srch)
 #            return Trains.objects.filter(user__is_active=True)
 #        return match
 #    else:
 #        return Trains.objects.filter(user__is_active=True)
	
	 # return render(request, "eticket/home.html",{'trains':trains}) 