from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf

def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'templates/Login/login.html', c)

