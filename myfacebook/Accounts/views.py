from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as syslogin
from .models import User

@csrf_protect
def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = 	form.get_user()
			syslogin(request, user)
			return redirect('/Home/');
	else:
		form = AuthenticationForm()
	return render(request, 'Accounts/login.html', {'form':form})

@csrf_protect
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST);
		if form.is_valid():
			user = form.save()
			syslogin(request, user)
			return redirect('/Home/');
	else:
		form = UserCreationForm()
	return render(request, 'Accounts/signup.html', {'form':form})


