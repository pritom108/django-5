from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='studentdelete'),
    path('delete1/<int:pk>/', views.StudentDeleteView1.as_view(), name='studentdelete1'),
    path('success/', TemplateView.as_view(template_name='myapp/success.html'), name='success'),
]
