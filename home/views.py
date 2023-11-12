from django.shortcuts import render
from products.models import Product
from testimonials.models import Testimonial

# Create your views here.

def Index(request):
    """ A view to return the index page """
    products = Product.objects.order_by('-id')[:3]
    testimonials = Testimonial.objects.all
    context = {
        'products': products,
        'testimonials': testimonials}
    return render(request, 'home/index.html', context)

