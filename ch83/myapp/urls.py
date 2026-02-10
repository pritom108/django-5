from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('create/', views.StudentCreateView.as_view(), name='studentcreate'), 
    path('create1/', views.StudentCreateView1.as_view(), name='studentcreate1'), 
    path('thanks/', TemplateView.as_view(template_name='myapp/thankyou.html'), name='thanks1'),   
]
