from django.shortcuts import render
from django.http import HttpResponse 
from .models import User
# Create your views here.

def index(request):
	all_scheds = User.objects.all()
	context = {'all_scheds': all_scheds}
	return render(request, 'schedule/index.html', context)

def detail (request, sched_id):
	return HttpResponse ('<h1> schedule for user ID: ' + sched_id + '</h1> ')


def update(request):
	return HttpResponse ('<h1> User goes here to view/change their schedule </h1>')

def intersect (request):
	return HttpResponse ('<h1> Select friends and compute intersection </h1>')