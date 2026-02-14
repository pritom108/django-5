from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home Page')

def htmlfun(request):
    return HttpResponse('<h1>Hello html</h1>')

def myfunction(request):
    return HttpResponse('Hello Django!')








