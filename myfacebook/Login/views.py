from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from .models import User

@csrf_protect
def login(request):
	c = {}
	c.update(csrf(request))
	alluser = User.objects.all()
	c['alluser'] = alluser
	return render(request, 'templates/Login/login.html', c)

