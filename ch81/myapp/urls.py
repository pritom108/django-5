from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.SingleStudentView.as_view(), name='single_student'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='studentdetail'),
    path('student1/<int:pritom>/',
         views.StudentDetailView1.as_view(), name='studentdetail1'),
    path('student2/<int:pk>/',
         views.StudentDetailView2.as_view(), name='studentdetail2'),
    path('student3/<int:pk>/', views.StudentDetailView3.as_view(),
         name='studentdetail3'),
]
