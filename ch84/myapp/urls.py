from django.urls import path
from myapp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('thanks/', TemplateView.as_view(template_name='myapp/thankyou.html'), name='thanks1'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update'),
    path('update1/<int:pk>/', views.StudentUpdateView1.as_view(), name='update1'),
    path('update2/<int:pk>/', views.StudentUpdateView2.as_view(), name='update2'),
]
