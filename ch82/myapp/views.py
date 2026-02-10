from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView
from .forms import ContactForm, StudentForm
from .models import Student
from django.contrib import messages


class ContactFormView(FormView):
    template_name = 'myapp/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'
    initial = {'name': 'Pritom', 'email': 'pritom@gmail.com'}

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        # return HttpResponse('Thank you Form Submitted!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'There was an error with your form submission.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = 'Hello FormView'
        return context


class StudentFormView(FormView):
    template_name = 'myapp/register.html'
    form_class = StudentForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        roll = form.cleaned_data['roll']
        course = form.cleaned_data['course']
        student = Student(
            name=name,
            roll=roll,
            course=course
        )
        student.save()
        return HttpResponse('Thank you Form Submitted!')

    def form_invalid(self, form):
        messages.error(
            self.request, 'There was an error with your form submission.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = 'Hello FormView'
        return context
