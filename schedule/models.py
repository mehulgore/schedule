from __future__ import unicode_literals

from django.db import models
#from django.contrib.postgres.fields import ArrayField 
# Create your models here.

class Schedule (models.Model):
	time_sheet = models.CharField(max_length=48)
	date = models.DateField(null=True)

