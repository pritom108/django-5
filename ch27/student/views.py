from django.shortcuts import render
from .forms import Registration, Login



def registration(req):
    fm =Registration()

    # fm =Registration(field_order=['email','city'])

    return render(req,'student/registration.html',{'form':fm})



def login(req):
    login =Login()
    return render(req,'student/login.html',{'form':login})


# def login(req):
    # login =Login(auto_id='log_%s')
    # login =Login(auto_id=True)
    # login =Login(auto_id=False)

    # login =Login(label_suffix=':')
    # login =Login(label_suffix=' ')

    # login = Login(initial={'email': 'Enter your email','password':'Enter password'})

    # login = Login(auto_id=True,label_suffix=':',initial={'email': 'Enter your email','password':'Enter password'})


    # return render(req,'student/login.html',{'form':login})