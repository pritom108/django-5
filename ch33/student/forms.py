from django import forms
from django.core import validators


def start_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Email should start with s')


# Clean and validaate Django form for field specific
class Registration(forms.Form):
    name = forms.CharField(error_messages={'required': 'Name is required'})
    email = forms.EmailField(error_messages={'required': 'Email is required'})
    password = forms.CharField(error_messages={'required': 'Password is required'},widget=forms.PasswordInput)
