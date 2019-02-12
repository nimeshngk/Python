from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url('', views.login),	# Main Login page
]