from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse('<h1>Hello Django</h1>')

def learn_django2(request, **kwargs):
    status = kwargs.get('status')
    return HttpResponse(f'<h1>Hello Django {status}</h1>')
