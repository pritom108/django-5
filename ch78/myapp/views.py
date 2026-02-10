from django.shortcuts import render
from django.views.generic.base import TemplateView



class AboutTemplateView(TemplateView):
    template_name = 'myapp/about.html'


class ContactTemplateView(TemplateView):
    template_name = 'myapp/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Pritom'
        context['roll'] = 108
        return context
    
class ContactTemplateView2(TemplateView):
    template_name = 'myapp/contact2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Pritom'
        context['roll'] = 108
        return context
    
class ProfileTemplateView(TemplateView):
    template_name = 'myapp/profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Pritom'
        print(context)
        print(kwargs)
        return context