# Generated by Django 3.2.21 on 2023-11-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0006_alter_workshops_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshops',
            name='spaces',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
