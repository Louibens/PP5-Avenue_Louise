from django.contrib import admin
from django.urls import path
from .views import Workshops

urlpatterns = [
    path('', Workshops.as_view(), name='workshops'),
]
