from django.shortcuts import render


def learn_django(request):
    seats = 10
    coursedetail = {'cname': 'Django', 'version': 5.1, 'seats': seats}
    # return render(request, 'course/django.html', context=coursedetail)
    # return render(request, 'course/django.html', {'cname': 'Django', 'version': 5.1, 'seats': seats})
    return render(request, 'course/django.html', coursedetail)
