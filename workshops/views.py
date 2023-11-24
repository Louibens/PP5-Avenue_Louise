from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .models import Workshops, WorkshopContact
from .forms import WorkshopsForm, WorkshopEnquiryForm
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)


class WorkshopsView(ListView):
    """View all workshops"""

    template_name = "workshops/workshops.html"
    model = Workshops
    context_object_name = "workshops"


class WorkshopDetail(DetailView):
    """View as a single workshop"""

    template_name = "workshops/workshop_detail.html"
    model = Workshops
    context_object_name = "workshop"


class AddWorkshop(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add workshop view"""

    template_name = "workshops/add_workshop.html"
    model = Workshops
    form_class = WorkshopsForm
    success_url = "/workshops/"
    success_message = 'Successfully added workshop!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddWorkshop, self).form_valid(form)


@login_required
def edit_workshop(request, workshop_id):
    """ Edit a workshop in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only shop owners can do that.')
        return redirect(reverse('home'))

    workshop = get_object_or_404(Workshops, pk=workshop_id)
    if request.method == 'POST':
        form = WorkshopsForm(request.POST, request.FILES, instance=workshop)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated workshop!')
            return redirect(reverse('workshop_detail', args=[workshop.id]))
        else:
            messages.error(request, 'Failed to update workshop. Please ensure the form is valid.')
    else:
        form = WorkshopsForm(instance=workshop)
        messages.info(request, f'You are editing {workshop.name}')
        
    template = 'workshops/edit_workshop.html'
    context = {
        'form': form,
        'workshop': workshop,
    }

    return render(request, template, context)


@login_required
def delete_workshop(request, workshop_id):
    """ Delete a workshop """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    workshop = get_object_or_404(Workshops, pk=workshop_id)
    if request.method == 'POST':
        workshop.delete()
        messages.success(request, 'Workshop deleted successfully.')
        return redirect(reverse('workshops'))

    template = 'workshops/workshop_confirm_delete.html'
    context = {
        'workshop': workshop,
    }
    
    return render(request, template, context)


def WorkshopRequest(request):
    """
    Form for user to enquire about workshops
    """
    if request.method == 'POST':
        form = WorkshopEnquiryForm(request.POST)
        if form.is_valid():
            workshop_request = form.save(commit=False)
            workshop_request.save()
            return render(request, 'workshops/workshop_request_success.html')
    else:
        if request.user.is_authenticated:
            form = WorkshopEnquiryForm(initial={'email': request.user.email})
        else:
            form = WorkshopEnquiryForm()
    return render(request,
                  'workshops/workshop_request_form.html', {'form': form})
