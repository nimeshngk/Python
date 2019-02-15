from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^signup/$', views.signup, name="signup"),
	url(r'^login/$', views.login, name="login"),
	url('', views.login),	# Main Login page
]