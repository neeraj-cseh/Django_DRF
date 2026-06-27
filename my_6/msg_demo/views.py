from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def show_msg(request):
    messages.debug(request, "This is a debug message.")
    messages.info(request, "This is an info message.")

    return render(request, 'show_msg.html')