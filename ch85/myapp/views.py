from django.shortcuts import render
from django.views.generic.edit import DeleteView
from .models import Student


class StudentDeleteView(DeleteView):
    model = Student
    # default template => student_confirm_delete.html
    success_url = '/success/'

class StudentDeleteView1(DeleteView):
    model = Student
    success_url = '/success/'
    template_name = 'myapp/student.html'
