from django.contrib import admin
from django.urls import path
from .views import WorkshopsView, AddWorkshop, WorkshopDetail

urlpatterns = [
    path('', WorkshopsView.as_view(), name='workshops'),
    path("add/", AddWorkshop.as_view(), name="add_workshop"),
    path("<slug:pk>/", WorkshopDetail.as_view(), name="workshop_detail"),
]
