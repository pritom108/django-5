from django.urls import path
from .views import registration, login

urlpatterns = [
    path('register/', registration),
    path('login/', login),
]