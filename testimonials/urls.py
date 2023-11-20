from django.contrib import admin
from django.urls import path
from . import views
from .views import TestimonialsView, AddTestimonial

urlpatterns = [
    path('', TestimonialsView.as_view(), name='testimonials'),
    path("add/", AddTestimonial.as_view(), name="add_testimonial"),
]
