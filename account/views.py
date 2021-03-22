from django.shortcuts import render , redirect
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout


def register(request):
      if request.method == 'POST':
            username = request.POST['user_name']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            age = request.POST['age']
            phone = request.POST['phone_no']
            gender = request.POST['gender']
            dob = request.POST['dob']
            aadharproof = request.FILES['aadhar_proof']
            state = request.POST['state']
            country = request.POST['country']
            maritalstatus = request.POST['marital_status']
            password = request.POST['password']
            password1 = request.POST['password1']



            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            
            account = Account(user=user,age=age,phone=phone,gender=gender,dob=dob,aadharproof=aadharproof,state=state,country=country,maritalstatus=maritalstatus)
            account.save()
            return redirect('/account/login/')
      return render(request, 'account/register.html')

def logins(request):
      if not request.user.is_authenticated:
            if request.method=="POST":
                  username=request.POST['user_name']
                  password=request.POST['password']
                  user=authenticate(request,username=username,password=password) 
            # if user is not None:
            #     login(request,user)
            #     if request.user.is_superuser:
            #         return redirect('/bazzar/add-product') 
            #     else:
                  return redirect('/eticket/home/')
            return render(request,'account/login.html')
      else:
            return redirect('/eticket/home/')            
 

def logout_view(request):
    logout(request)
    return redirect("/account/login/")
      
# Create your views here.
