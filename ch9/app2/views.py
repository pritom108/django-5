from django.shortcuts import render
from django.http import HttpResponse

def myapp2(request):
    return HttpResponse('<h1>Hello App 2</h1>')
