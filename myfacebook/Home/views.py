from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def homepage(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'templates/Home/homepage.html', c)
