from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def authentication(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = authenticate(username=username, password=password)
		login(request,user)
		return redirect('/')
	return render(request,'login.html', {})

def home(request):
	return render(request, 'home.html', {})

def signup(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = User.objects.create_user(username=username, password=password)
		user.save()
		return redirect('/login')
	return render(request,'signup.html', {})
