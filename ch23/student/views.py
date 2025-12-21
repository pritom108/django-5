from django.shortcuts import render
from .models import Profile

def all_data(req):
    all_students = Profile.objects.all()
    return render(req,'student/all.html',{'students':all_students})

def single_data(req):
    single_student= Profile.objects.get(pk=1)
    return render(req,'student/single.html',{'student':single_student})
