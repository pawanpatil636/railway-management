from django.urls import path
from .import views


app_name="train"
urlpatterns=[
    path('trains-list/',views.search_train, name='trains_list'),
]