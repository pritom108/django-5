from django import forms
from django.core import validators


def start_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Email should start with s')


# Clean and validaate Django form for field specific
class Registration(forms.Form):
    name = forms.CharField(validators=[
        validators.MaxLengthValidator(12),
        validators.MinLengthValidator(4),
    ])
    email = forms.EmailField(validators=[start_with_s])
    password = forms.CharField(widget=forms.PasswordInput)
