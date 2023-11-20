from django.shortcuts import render
from products.models import Product
from testimonials.models import Testimonial
from .forms import ContactUsForm

# Create your views here.

def Index(request):
    """ A view to return the index page """
    products = Product.objects.order_by('-id')[:3]
    testimonials = Testimonial.objects.all
    context = {
        'products': products,
        'testimonials': testimonials}
    return render(request, 'home/index.html', context)


def AboutUs(request):
    testimonials = Testimonial.objects.all
    context = {
        'testimonials': testimonials}
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            contact_request = form.save(commit=False)
            contact_request.save()
            return render(request, 'home/about_us.html')
    else:
        if request.user.is_authenticated:
            form = ContactUsForm(initial={'email': request.user.email})
        else:
            form = ContactUsForm()
    context['form'] = form
    return render(request, 'home/about_us.html', context)


def ContactUs(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            contact_request = form.save(commit=False)
            contact_request.save()
            return render(request, 'home/contact_us_request_success.html')
    else:
        if request.user.is_authenticated:
            form = ContactUsForm(initial={'email': request.user.email})
        else:
            form = ContactUsForm()
    return render(request, 'home/contact_us.html', {'form': form})