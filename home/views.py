from django.shortcuts import render
from products.models import Product

# Create your views here.

def Index(request):
    """ A view to return the index page """
    products = Product.objects.order_by('-id')[:3]
    context = {'products': products}
    return render(request, 'home/index.html', context)

