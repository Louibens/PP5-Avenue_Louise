from django.contrib import admin
from django.urls import path
from . import views
from .views import workshops

urlpatterns = [
    path('', views.workshops, name='workshops'),
]
