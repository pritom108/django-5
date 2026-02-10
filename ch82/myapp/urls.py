from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('thanks/', TemplateView.as_view(template_name='myapp/thankyou.html'), name='thanks'),
    path('register/', views.StudentFormView.as_view(), name='register'),
]
