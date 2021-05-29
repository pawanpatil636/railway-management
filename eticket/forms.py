from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SearchForm(forms.Form):
	src = forms.CharField(max_length=20)
	dest = forms.CharField(max_length=20)