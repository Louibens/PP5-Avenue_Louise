from django.db import models

# Create your models here.

class Workshops(models.Model):
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
        return self.title