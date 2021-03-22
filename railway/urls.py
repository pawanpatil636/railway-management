
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include("account.urls",namespace="account")),
    path('eticket/',include("eticket.urls",namespace="eticket")),
    path('train/',include("train.urls",namespace="train")),
]
