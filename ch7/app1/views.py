from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home Page')


def myapp1(request):
    return HttpResponse('My App 1 Page')
