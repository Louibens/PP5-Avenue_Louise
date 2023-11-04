from django.contrib import admin
from django.urls import path
from . import views
from .views import WorkshopsView, AddWorkshop, WorkshopDetail, WorkshopRequest

urlpatterns = [
    path('', WorkshopsView.as_view(), name='workshops'),
    path("add/", AddWorkshop.as_view(), name="add_workshop"),
    path("<int:pk>/", WorkshopDetail.as_view(), name="workshop_detail"),
    path('edit/<int:workshop_id>/', views.edit_workshop, name='edit_workshop'),
    path('delete/<int:workshop_id>/', views.delete_workshop, name='delete_workshop'),
    path('request/', views.WorkshopRequest, name='request'),
]
