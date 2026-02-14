from django.shortcuts import render
from datetime import datetime

# Example 1.1 - Variable
def learn_django(request):
    return render(request, 'course/django.html', context={'name': 'Django'})

# Example 1.2 - Variable
def learn_django(request):
    name = 'Django'
    duration = '4 months'
    seats = 10
    course_details = {'nm': name, 'du': duration, 'st': seats}
    return render(request, 'course/django.html', course_details)

# Example 2 - Filter
def learn_django(request):
    return render(request, 'course/django.html', context={'name': 'Django', 'desc': 'Django is awsome web framework'})

# Example 3 - Date and Time
def learn_django(request):
    d = datetime.now()
    return render(request, 'course/django.html', context={'dt': d})

# Example 4 - Float Format
def learn_django(request):
    return render(request, 'course/django.html', context={'p1': 56.24321, 'p2': 56.000, 'p3': 56.37000})

# Example 5.1 - If Tag
def learn_django(request):
    # (nm = '' ==> False ) (nm = 'ldlfs' ==> True)
    return render(request, 'course/django.html', context={'nm': True})

# Example 5.2 - If Tag
def learn_django(request):
    return render(request, 'course/django.html', context={'nm': 'Django', 'st': 5})

# Example 6 - For loop 
def learn_django(request):
    students = {'names': ['Rahul', 'Sonam', 'Raj', 'Anu']}
    return render(request, 'course/django.html', context=students)

# Example 7 - Complex data 
def learn_django(request):
    stu = {'stu1': {'name': 'Rahul', 'roll': 101},
           'stu2': {'name': 'Sonam', 'roll': 102},
           'stu3': {'name': 'Raj', 'roll': 103},
           'stu4': {'name': 'Anu', 'roll': 104},
           }
    students = {'students': stu}
    return render(request, 'course/django.html', context=students)


# Example 8 - Complex data
def learn_django(request):
    student = {'name': 'Rahul', 'roll': 101}
    return render(request, 'course/django.html', context={'student': student})


# Example 9 - Complex data
def learn_django(request):
    stu = {'stu1': {'name': 'Rahul', 'roll': 101},
           'stu2': {'name': 'Sonam', 'roll': 102},
           'stu3': {'name': 'Raj', 'roll': 103},
           'stu4': {'name': 'Anu', 'roll': 104},
           }
    return render(request, 'course/django.html', {'students':stu})