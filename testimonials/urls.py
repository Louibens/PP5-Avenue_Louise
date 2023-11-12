from django.contrib import admin
from django.urls import path
from . import views
from .views import TestimonialsView

urlpatterns = [
    path('', TestimonialsView.as_view(), name='testimonials'),
]
