from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse ("Home Page")

def myfunction(request):
    return HttpResponse('Hello Django')

def django_index(req):
    return render(req, 'app1/django.html')