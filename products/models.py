from django.db import models
from django_resized import ResizedImageField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    height = models.DecimalField(max_digits=4, decimal_places=2)
    width = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = ResizedImageField(
        size=[None, 400],
        quality=75,
        upload_to="products/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def change_in_stock(self):
        """ automatically change stock label """
        if self.count == 0:
            self.in_stock = False
        else:
            self.in_stock = True
        self.save()