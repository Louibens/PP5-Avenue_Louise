from django.contrib import admin
from .models import Workshops, WorkshopContact

# Register your models here.
admin.site.register(Workshops)

@admin.register(WorkshopContact)
class WorkshopContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',
                    'workshop_enquiry')
    search_fields = ('name', 'email',
                     'workshop_enquiry')
