from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('myfun/', views.myfunction, name='myfunction'),
    path('html/',views.htmlfun, name='htmlfun'),
]
