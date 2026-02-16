from django.urls import path
from core.views import home, about, menu, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('contact/', contact, name='contact'),
]
