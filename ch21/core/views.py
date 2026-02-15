from django.shortcuts import render

def home(req):
    return render(req, 'core/home.html',{'list_element': 'Python'})

def about(req):
    return render(req, 'core/about.html')
