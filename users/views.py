from django.shortcuts import render
from django.contrib.auth.models import User
from djando.contrib.auth import authenticate, login

# Create your views here.

def authentication(request):
	