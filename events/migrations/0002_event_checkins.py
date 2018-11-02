# Generated by Django 2.1.2 on 2018-11-01 20:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='checkins',
            field=models.ManyToManyField(related_name='checked_in', to=settings.AUTH_USER_MODEL),
        ),
    ]