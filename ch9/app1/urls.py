from django.urls import path
from app1.views import learn_django, learn_django2

urlpatterns = [
    path('py/',learn_django),
    path('dj/', learn_django2, {'status': 'OK'})
]