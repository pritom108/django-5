from django.urls import path
from django.views.generic.base import TemplateView, RedirectView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='myapp/home.html'), name='home'),
    path('home/', RedirectView.as_view(url='/'), name='home1'),
    path('index/', views.RedirectView.as_view(url='/'), name='index'),
    path('index2/', views.RedirectView.as_view(pattern_name='home'), name='index2'),
    path('newhome/', views.NewHomeRedirectView.as_view(), name='newhome'),

    path('profile/<int:pk>/', TemplateView.as_view(template_name='myapp/profile.html'), name='profile'),
    path('login/', TemplateView.as_view(template_name='myapp/login.html'), name='login'),

    path('success/<int:pk>/', views.SuccessRedirectView.as_view(), name='success'),

]
