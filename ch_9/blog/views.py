from django.shortcuts import render
from datetime import datetime


def blog_details(request):
    post = {
        "name" : "Neeraj Srinivas",
        "age" : 23,
    }
    return render(request, 'blog/blog_details.html', {"post": post})