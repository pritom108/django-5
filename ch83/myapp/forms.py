from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']

        # only for StudentCreateView1
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myclass'}),
            'password': forms.PasswordInput(attrs={'class': 'mypass'})
        }
