from django.urls import path
from .import views

app_name="eticket"
urlpatterns = [
    path("home/", views.home , name="home"),
    path("search-result/", views.srch , name="search_result"),
    path("passenger-details/",views.passenger_details, name="passenger_details"),
    path("user-account/",views.user_account, name="user-account"),
    ]