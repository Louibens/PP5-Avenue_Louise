from django.urls import path
from . import views
from .views import AboutUs, ContactUs

urlpatterns = [
    path('', views.Index, name='home'),
    path('aboutus/', views.AboutUs, name='aboutus'),
    path('contactus/', views.ContactUs, name='contactus'),
]
