from django.views.generic import ListView, CreateView
from django.views import generic
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from .models import Testimonial
from .forms import testimonialForm
from django.urls import reverse_lazy


class TestimonialsView(ListView):
    """View all testimonials"""

    template_name = "testimonials/testimonials.html"
    model = Testimonial
    context_object_name = "testimonials"


class AddTestimonial(LoginRequiredMixin, CreateView):
    """Add testimonial """

    template_name = "testimonials/add_testimonial.html"
    model = Testimonial
    form_class = testimonialForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddTestimonial, self).form_valid(form)