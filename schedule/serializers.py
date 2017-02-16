from rest_framework import serializers 
from .models import Schedule

class ScheduleSerializer (serialzers.ModelSerializer):
	class Meta: 
		model = Schedule
		fields = '__all__'