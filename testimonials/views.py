from django.views.generic import ListView
from django.views import generic
from .models import Testimonial


class TestimonialsView(ListView):
    """View all testimonials"""

    template_name = "testimonials/testimonials.html"
    model = Testimonial
    context_object_name = "testimonials"
