from __future__ import unicode_literals
from django.db import models

class User(models.Model):
	user_name = models.CharField(max_length=50)
	user_id = models.CharField(max_length=20)
	password = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)

	def __str__(self):
		return self.user_name