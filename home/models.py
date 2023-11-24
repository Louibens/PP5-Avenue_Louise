from django.db import models


class ContactUs(models.Model):
    """ Model for general contact form"""
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    message = models.TextField(max_length=600, default='')

    def __str__(self):
        return self.name
