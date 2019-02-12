from __future__ import unicode_literals
from django.shortcuts import render
from django.template.context_processors import csrf

def timeline(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'templates/Timeline/timeline.html')
