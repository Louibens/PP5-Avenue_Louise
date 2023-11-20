from django.urls import path
from . import views
from .views import AboutUs

urlpatterns = [
    path('', views.Index, name='home'),
    path('aboutus/', views.AboutUs, name='aboutus'),
]
