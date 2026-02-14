
from django.urls import path
from .views import learn_django, learn_django_template

urlpatterns = [
    path('dj/', learn_django),
    path('dj_temp/', learn_django_template),
]
