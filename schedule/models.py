from __future__ import unicode_literals

from django.db import models
#from django.contrib.postgres.fields import ArrayField 
# Create your models here.

class User (models.Model):
	username = models.CharField(max_length=100)
	time_sheet = models.TextField(max_length=200)

	def __str__ (self):
		return self.username + ' - ' + self.time_sheet