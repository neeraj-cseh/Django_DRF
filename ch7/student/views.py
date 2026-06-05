from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'student/home.html')

def profile(req, my_class, my_id):
    student = {'id' : my_id, 'class': my_class}
    return render(req, 'student/profile.html', {'student': student})