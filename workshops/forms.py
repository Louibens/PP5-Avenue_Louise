from django import forms
from .models import Workshops


class WorkshopsForm(forms.ModelForm):
    """Form to create a workshop"""

    class Meta:
        model = Workshop
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
        }
