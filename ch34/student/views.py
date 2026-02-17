from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']

            # Save Data into Database
            user = Profile(name=nm, email=em, password=pw)
            user.save()

            # Update Data into Database
            # user = Profile(id=1, name=nm, email=em, password=pw)  # This is hardcoded id. But in actual id will come from pk
            # user.save()
            
            # Save Data into Database
            # user = Profile(id=1)  # This is hardcoded id. But in actual id will come from pk
            # user.delete()

            return HttpResponseRedirect('/student/register/')
    else:
        form = Registration(request.POST)
        print(form)

    return render(request, 'student/register.html', {'form': form})
