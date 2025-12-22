from django.urls import path
from .views import demo_form

urlpatterns = [
    path('demo_form/', demo_form, name="demo_form"),
]