from django import forms
from .models import Workshops, WorkshopContact
import textwrap


class WorkshopsForm(forms.ModelForm):
    """Form to create a workshop"""

    class Meta:
        model = Workshops
        fields = [
            "name",
            "description",
            "price",
            "location",
            "date",
            "spaces",
            "image",
        ]

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "name": "Workshop Name",
            "description": "Description",
            "price": "Workshop price",
            "location": "Workshop Location",
            "date": "Workshop Date",
            "space": "Spaces",
            "image": "Workshop Image",

        }


class WorkshopEnquiryForm(forms.ModelForm):
    """Form for site user to contact the site owner about workshop enquiries"""
    class Meta:
        model = WorkshopContact
        fields = ['name', 'email', 'workshop', 'workshop_enquiry']

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

        self.fields['workshop'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Select a workshop'
        })

        self.fields['workshop_enquiry'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': textwrap.dedent('''\
                Enter your workshop enquiry and we will get back to you with further information and booking details
                ''')
        })
