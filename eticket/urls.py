from django.urls import path
from .import views

app_name="eticket"
urlpatterns  =[
    path("home/", views.home , name="home"),
    ]