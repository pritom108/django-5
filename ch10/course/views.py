from django.shortcuts import render
from django.http import HttpResponse


def learn_django(req):
    html = '<h1>Hello Django from Course App</h1>'
    return HttpResponse(html)


def learn_django_template(request):
    # render(request, template_name, context = dict_name, content_type = MIME_TYPE, status = None, using = None)
    return render(request, 'course/django.html')
