from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from .models import Student


class SingleStudentView(View):
    def get(self, request, pk):
        single_student = Student.objects.get(pk=pk)
        return render(request, 'myapp/single_student.html', {'single_student': single_student})


class StudentDetailView(DetailView):
    model = Student


class StudentDetailView1(DetailView):
    model = Student
    pk_url_kwarg = 'pritom'
    # template_name_suffix = '_single'
    # template_name = 'myapp/student.html'


class StudentDetailView2(DetailView):
    model = Student
    template_name = 'myapp/student.html'
    context_object_name = 'stu'


class StudentDetailView3(DetailView):
    model = Student
    template_name = 'myapp/student2.html'
    context_object_name = 'stu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all().order_by('name')
        return context
