from django import forms
from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description',
                  'genre', 'isbn', 'publication_date']

        # Tailwind classes for all fields
        common_classes = (
            "w-full px-4 py-3 bg-white border-2 border-purple-200 rounded-xl "
            "focus:outline-none focus:ring-4 focus:ring-purple-300 focus:border-purple-500 "
            "shadow-sm placeholder-gray-400"
        )

        widgets = {
            'title': forms.TextInput(attrs={
                'class': common_classes,
                'placeholder': 'Enter book title'
            }),
            'author': forms.TextInput(attrs={
                'class': common_classes,
                'placeholder': 'Enter author name'
            }),
            'description': forms.Textarea(attrs={
                'class': f"{common_classes} h-32",
                'placeholder': 'Enter book description'
            }),
            'genre': forms.Select(attrs={
                'class': common_classes
            }),
            'isbn': forms.TextInput(attrs={
                'class': common_classes,
                'placeholder': 'Enter ISBN'
            }),
            'publication_date': forms.DateInput(attrs={
                'class': common_classes,
                'type': 'date'
            }),
        }
