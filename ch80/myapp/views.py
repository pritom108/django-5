from django.shortcuts import render
from django.views import View
from .models import Student
from django.views.generic.list import ListView


class AllStudentView(View):
    def get(self, request):
        all_students = Student.objects.all()
        return render(request, 'myapp/all_student.html', {'all_students': all_students})


class StudentListView(ListView):
    model = Student


class StudentListView1(ListView):
    model = Student
    template_name_suffix = '_all'
    ordering = ['name']


class StudentListView2(ListView):
    model = Student
    template_name = 'myapp/students.html'
    context_object_name = 'students'


class StudentListView3(ListView):
    model = Student
    template_name = 'myapp/editstudents.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course='Python')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['eee_students'] = Student.objects.filter(course='EEE')
        return context
    
    def get_template_names(self):
        if self.request.COOKIES.get('user') == 'pritom':
            template_name = 'myapp/pritom.html'
        else:
            template_name = self.template_name
        return [template_name]
