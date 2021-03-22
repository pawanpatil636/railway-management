from django.contrib import admin
from .models import Stations
from .models import Trains


admin.site.register(Stations)
admin.site.register(Trains)
# Register your models here.
