from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Workshops(models.Model):
    """ Model for workshops"""
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=254)
    date = models.DateTimeField()
    spaces = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name


class WorkshopContact(models.Model):
    """ Model for contact form about workshops"""

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    workshop = models.ForeignKey(Workshops, on_delete=models.SET_NULL, null=True, default="")
    workshop_enquiry = models.TextField(max_length=600, default='')

    def __str__(self):
        return self.name