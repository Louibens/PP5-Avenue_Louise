from django.shortcuts import render
from .models import Workshops

# Create your views here.

def workshops(request):
    """ A view to show all workshops includng sorting and search queries """

    workshops = Workshops.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('workshops'))
            
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        workshops = workshops.filter(queries)

    context = {
        'workshops': workshops,
        'search_term': query,
    }

    return render(request, 'workshops/workshops.html', context)
