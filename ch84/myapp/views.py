from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Student
from django import forms
from .forms import StudentForm


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = '/thanks/'
    # default template name = student_form.html


# custom template
class StudentUpdateView1(UpdateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = '/thanks/'
    template_name = 'myapp/register.html'

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(
            attrs={'class': 'myclass'})
        form.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'mypass'})
        return form


# Using Model Form
class StudentUpdateView2(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = '/thanks/'
    template_name = 'myapp/register.html'
