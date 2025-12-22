from django.shortcuts import render
from .forms import DemoForm



def demo_form(req):
    form = DemoForm()
    return render(req,'student/demoform.html',{'form':form})
