from django.shortcuts import render
from datetime import datetime

# Create your views here.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def home(request):
    context = {
        'name' : 'Neeraj Srinivas', 
        'age' : 23, 
        'skills' : ['Python', 'Django', 'JavaScript'],
        'user' : User('Srinivas', 23),
        'blog' : {
            'title' : 'Django Template Intro',
            'content' : '<b>This is bold.</b>',
            'created_at' : datetime.now(),
        },
        'empty_value' : None,
        # 'empty_value' : 'None',
         }
    return render(request, 'blog/home.html', context)