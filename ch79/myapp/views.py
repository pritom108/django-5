from django.shortcuts import render
from django.views.generic.base import RedirectView


class NewHomeRedirectView(RedirectView):
    # url='/'
    pattern_name = 'home'


class SuccessRedirectView(RedirectView):
    pattern_name = 'profile'
    query_string = True # To send query with url
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)
