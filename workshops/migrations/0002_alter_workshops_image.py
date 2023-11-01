# Generated by Django 3.2.21 on 2023-11-01 17:59

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshops',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='No image', force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='workshops/'),
        ),
    ]
