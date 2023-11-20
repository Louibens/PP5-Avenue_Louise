from django import forms
from .models import Testimonial


class testimonialForm(forms.ModelForm):
    """
    Form to add testimonial.
    """
    class Meta:
        """
        Form has all required fields from Testimonial model
        """
        model = Testimonial
        fields = ('client_name', 'client_testimonial',
                  'image')


