from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Testimonial(models.Model):
    """
    Model class for the testimonials app
    """
    client_name = models.CharField(max_length=250)
    client_testimonial = models.TextField(blank=True, null=True)
    image = ResizedImageField(
        size=[None, 400],
        quality=75,
        upload_to="testimonials/",
        force_format="WEBP",
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.client_name
