# from django.shortcuts import render, redirect
# from django.http import HttpResponse 
# from .models import Schedule
# from django.http import Http404
# from django.contrib.auth import authenticate, login

# from .forms import UserForm
# from django.views import generic 
# Create your views here.

# def index(request):
# 	return render(request, 'index.html', {})

# def detail (request, user_id):
# 	try:
# 		user = User.objects.get(pk=user_id)
# 	except User.DoesNotExist:
# 		raise Http404("User does not exist you idiot")
# 	return HttpResponse ('<h1> user: ' + user.username + '</h1> ')

# def intersect (request):
# 	return HttpResponse ('<h1> Select friends and compute intersection </h1>')

# def data (request):
# 	users = User.objects.all()
# 	context = {'users': users}
# 	return render(request, 'displaydata.html', context)

#def submit (request, date, sched): 

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.views import generic 
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Schedule
from .serializers import ScheduleSerializer 
from django.contrib.auth.models import User


class InputView(TemplateView):
	template_name = 'index.html'

	def get(self, request):
		username = None
    	if request.user.is_authenticated():
        	username = request.user.username
		context = {'username': username}
		return render(request, self.template_name, context)

	def post(self, request):
		return render(request, self.template_name, context)

class UserFormView(View):
	form_class = UserForm
	template_name = 'register_form.html'

	def get(self, request):
		form = self.form_class(None)
		context = {'form': form}
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid(): 
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username = username, password = password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('schedule:index')

		context = {'form': form, 'username': username}

		return render(request, self.template_name, context)






