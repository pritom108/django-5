from django.urls import path
from .views import learn_django, learn_python

urlpatterns = [
    path('dj/', learn_django, name='django'),
    path('py/', learn_python, name='python'),
]
