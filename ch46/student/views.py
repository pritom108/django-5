from django.shortcuts import render
from datetime import datetime, timedelta, timezone


def setcookie(request):
    response = render(request, 'student/setcookie.html')

    # browser close cookie delete
    response.set_cookie('pay_id', 't123456')  

    # after 1 hour cookie will delete but not in browser close
    # response.set_cookie('pay_id', 't123456', max_age=3600)  

    # after 2 days from now cookie will delete 
    # response.set_cookie('pay_id', 't123456', expires=datetime.now(timezone.utc) + timedelta(days=2))

    return response

def getcookie(request):
    # pay_id = request.COOKIES['pay_id']
    # pay_id = request.COOKIES.get('pay_id', 'default_pay_id') # If cookie value is None then default value will be shown
    pay_id = request.COOKIES.get('pay_id')
    return render(request, 'student/getcookie.html', {'pay_id': pay_id})

def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('pay_id')
    return response


def setsignedcookie(request):
    response = render(request, 'student/setsignedcookie.html')
    response.set_signed_cookie('token', 't12345', salt='tk')
    return response

def getsignedcookie(request):
    token = request.get_signed_cookie('token', salt='tk')
    # token = request.get_signed_cookie('token', default='default_token', salt='tk')
    return render(request, 'student/getsignedcookie.html',{'token': token})