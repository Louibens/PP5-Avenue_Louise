from django.shortcuts import render

from django.views.generic import ListView
from .models import Workshops
# Create your views here.


class Workshops(ListView):
    """View all workshops"""

    template_name = "workshops/workshops.html"
    model = Workshops
    context_object_name = "workshops"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            workshops = self.model.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query))
        else:
            workshops = self.model.objects.all()
        return workshops
