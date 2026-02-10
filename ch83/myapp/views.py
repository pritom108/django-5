from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django import forms
from .forms import StudentForm


class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    # success_url = '/thanks/' # we defined get_absolute_url in model.py file
    # default template name student_form
    template_name = 'myapp/register.html'

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(
            attrs={'class': 'myclass'})
        form.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'mypass'})
        return form
    
class StudentCreateView1(CreateView):
    form_class = StudentForm
    template_name = 'myapp/student_form.html'
    # success url is from model.py file's get_absolute_url function
