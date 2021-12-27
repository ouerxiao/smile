# Generated by Django 3.1 on 2020-09-05 19:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0019_postimage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='likes_image',
            field=models.ManyToManyField(blank=True, related_name='likes_image', to=settings.AUTH_USER_MODEL),
        ),
    ]
