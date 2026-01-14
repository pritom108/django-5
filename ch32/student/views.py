from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.POST['name'])
        form = Registration(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            # print(form.cleaned_data)
            return HttpResponseRedirect('/student/success/')
    else:
        form = Registration(request.POST)
        print(form)

    return render(request, 'student/register.html', {'form': form})


def reg_success(request):
    return render(request,'student/success.html')
