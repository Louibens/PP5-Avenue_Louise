from django.shortcuts import render

from django.views.generic import CreateView, ListView

from .models import Workshops
from .forms import WorkshopsForm

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
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


class AddWorkshop(LoginRequiredMixin, CreateView):
    """Add workshop view"""

    template_name = "workshops/add_workshop.html"
    model = Workshops
    form_class = WorkshopsForm
    success_url = "/workshops/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddWorkshop, self).form_valid(form)
