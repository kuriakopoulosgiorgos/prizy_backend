# Generated by Django 2.1.2 on 2018-11-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='checked_in',
            field=models.ManyToManyField(to='events.Event'),
        ),
    ]