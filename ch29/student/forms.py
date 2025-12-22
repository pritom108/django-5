from django import forms
from django.core.validators import MinLengthValidator, RegexValidator


# class DemoForm(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()
#     pin_code=forms.IntegerField()

#     age=forms.FloatField()
#     date_of_birth=forms.DateField()
#     appointment_time=forms.TimeField()
#     appointment_datetime=forms.TimeField()
#     is_subscribed=forms.BooleanField()
#     agree_terms=forms.NullBooleanField()

#     #choice field
#     gender=forms.ChoiceField(choices=[('M','Male'),('F','Female'),('O','Other')])
#     interests=forms.MultipleChoiceField(choices=[('tech','Technology'),('art','Art'),('sports','Sports')])

#     # File and URL Fields
#     profile_image =forms.ImageField()
#     resume=forms.FileField()
#     website=forms.URLField()

#     # Other Specialized Fields
#     phone_number=forms.RegexField(regex=r'^\+?1?\d{9,15}$')
#     password=forms.CharField(widget=forms.PasswordInput())
#     slug=forms.SlugField()
#     ip_address=forms.GenericIPAddressField()
#     rating=forms.DecimalField()







class DemoForm(forms.Form):
    name=forms.CharField(
        label="Full Name",
        max_length=100,
        label_suffix=":",
        initial="Enter your full name",
        help_text="Enter your legal name here",
        validators=[MinLengthValidator(3)],
        required=True
    )
    email=forms.EmailField(
        label="Email Address",
        disabled=True
    )
    pin_code=forms.IntegerField(
        label="Pin Code",
        min_value=100000,
        max_value=999999,
        error_messages={
            'min_value': 'Pin code must be at least 6 digits.',
            'max_value': 'Pin code must be at most 6 digits.'
        }
    )

    age=forms.FloatField(
        label="Age",
        min_value=0
    )
    date_of_birth=forms.DateField(
    )
    appointment_time=forms.TimeField()
    appointment_datetime=forms.TimeField()
    is_subscribed=forms.BooleanField()
    agree_terms=forms.NullBooleanField()

    #choice field
    gender=forms.ChoiceField(choices=[('M','Male'),('F','Female'),('O','Other')])
    interests=forms.MultipleChoiceField(choices=[('tech','Technology'),('art','Art'),('sports','Sports')])

    # File and URL Fields
    profile_image =forms.ImageField()
    resume=forms.FileField()
    website=forms.URLField()

    # Other Specialized Fields
    phone_number=forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    password=forms.CharField(widget=forms.PasswordInput())
    slug=forms.SlugField()
    ip_address=forms.GenericIPAddressField(
        label="IP Address",
        protocol='both',
        unpack_ipv4=False,
        localize=True
    )
    rating=forms.DecimalField(
        label="Rating",
        max_digits=3,
        decimal_places=1,
        min_value=0,
        max_value=10,
        initial=5.0,
        help_text="Provide a rating between 0 and 10",
        localize=True
    )
    dob=forms.DateField(
        label="Date Field",
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )
    meeting_time=forms.TimeField(
        label="Time Field",
        widget=forms.TimeInput(attrs={'placeholder': 'HH:MM:SS'})
    )
    datetime_field=forms.DateTimeField(
        label="DateTime Field",
        widget=forms.DateTimeInput(
            attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}
        )
    )

    url=forms.URLField(
        widget=forms.URLInput(
            attrs={'placeholder': 'https://example.com'}
        )
    )

    post_content=forms.CharField(
        widget=forms.Textarea(
            attrs={'placehoder': 'Enter multiple lines of text ...'}
        )
    )

    multiple_choice_field=forms.MultipleChoiceField(
        label="Multiple Choice Field",
        widget=forms.SelectMultiple()
    )


