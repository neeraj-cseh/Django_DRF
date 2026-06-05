from django.contrib import admin
from django.urls import path, include
from student.views import home, profile

urlpatterns = [
    path('home/', home),
    path('profile/<int:my_class>/<int:my_id>/', profile, name='profile'),
]
