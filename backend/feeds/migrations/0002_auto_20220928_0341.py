# Generated by Django 3.2.8 on 2022-09-28 03:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='feeds', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]
