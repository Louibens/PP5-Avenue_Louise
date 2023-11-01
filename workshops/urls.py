from django.contrib import admin
from django.urls import path
from .views import Workshops, AddWorkshop

urlpatterns = [
    path('', Workshops.as_view(), name='workshops'),
    path("add/", AddWorkshop.as_view(), name="add_workshop"),
]
