from django.shortcuts import render
from .models import Student
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'roll']
    success_url = '/student/'
    # default template = student_form.html
    # template_name = 'myapp/student_form.html'


class StudentListView(ListView):
    model = Student
    # default context name => student_list or object_list
    context_object_name = 'students'
    # default template = student_list.html


class StudentDetailView(DetailView):
    model = Student
    # default context name => student or object
    context_object_name = 'student'
    # default template = student_detail.html


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'roll']
    success_url = '/student/'
    # default template = student_form.html


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/student/'
    # default template = student_confirm_delete.html
