from django.shortcuts import render

def learn_django(req):
    return render(req, 'course/django.html')

def learn_python(req):
    return render(req, 'course/python.html')