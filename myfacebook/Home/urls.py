from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url('', views.homepage),	# Main Login page
]