from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfunc1(request):
    return HttpResponse("Hello World")

def myfunc2(request):
    return HttpResponse("Hello World")

def home(request, **kwargs):
    status = kwargs.get('status', 'No status provided')
    return HttpResponse(f"Home Page - Status: {status}")