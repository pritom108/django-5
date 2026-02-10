from django.shortcuts import render, HttpResponse
# from .forms import ContactForm
from django.views import View


# ===========================================================================
def myfunview1(request):
    return HttpResponse("Hello Function based View")
# -------------------------------------------------------------


class MyClassView1(View):
    def get(self, request):
        return HttpResponse("Hello Class based View")


# ===========================================================================
def myfunview2(request):
    return HttpResponse("<h1>Function Based View</h1>")
# ---------------------------------------------------------------


class MyClassView2(View):
    def get(self, request):
        return HttpResponse("<h1>Hello Class based View</h1>")


class MyClassView3(View):
    name = 'Pritom'

    def get(self, request):
        return HttpResponse(self.name)


class MyChildClassView3(MyClassView3):
    def get(self, request):
        return HttpResponse(self.name)


# ===========================================================================
def homefunview(request):
    return render(request, 'myapp/home.html')
# ------------------------------------------------------


class HomeClassView(View):
    def get(self, request):
        return render(request, 'myapp/home.html')


# ===========================================================================
def aboutfunview(request):
    context = {'msg': 'Welcome to Django 5'}
    return render(request, 'myapp/about.html', context)
# -----------------------------------------------------------


class AboutClassView(View):
    def get(self, request):
        context = {'msg': 'Welcome to Django 5'}
        return render(request, 'myapp/about.html', context)


# ===========================================================================
def newsfunview(request):
    context = {'info': 'Hello this is Django news'}
    return render(request, 'myapp/news.html', context)
# -----------------------------------------------------------


class NewsClassView(View):
    template_name = ''

    def get(self, request):
        context = {'info': 'Hello this is Django news'}
        return render(request, self.template_name, context)


# ===========================================================================
def newsfunview2(request, template_name):
    template_name = template_name
    context = {'info': 'Hello this is Django news'}
    return render(request, template_name, context)


# ===========================================================================
def contactfunview(request):
    pass
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data['name'])
    #         return HttpResponse('Thank you form submitted!!')
    #     else:
    #         form = ContactForm()
    #     return render(request, 'myapp/contact.html',{'form': form})
# --------------------------------------------------------------------------


class ContactClassView(View):
    pass
    # def get(self, request):
    #     form = ContactForm()
    #     return render(request, 'myapp/contact.html',{'form': form})

    # def post(self, request):
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data['name'])
    #         return HttpResponse('Thank you form submitted!!')
