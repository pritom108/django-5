from django.shortcuts import render
from django.http import HttpResponse

def myapp2(request):
    return HttpResponse('My App 2 Page')

def myapp2_me(request):
    return HttpResponse('My App 2 Me Page')
