from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_testimonial',
                     'image')
    search_fields = ('client_name', 'client_testimonial',
                     'image')
