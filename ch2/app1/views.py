from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun(request):
    name = 'Neeraj'
    return HttpResponse(f'Hello {name}')

def index1(req):
    sname = 'Neeraj'
    details = {'sname' : sname}
    return render(req, 'app1/index.html', details)

