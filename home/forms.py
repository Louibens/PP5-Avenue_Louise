from django import forms
from .models import ContactUs
import textwrap


class ContactUsForm(forms.ModelForm):
    """Form for site user to contact the shop"""
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })

        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': textwrap.dedent('''\
                Enter your message
                ''')
        })
