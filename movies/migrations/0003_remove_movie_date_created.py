# Generated by Django 5.1 on 2024-08-27 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date_created',
        ),
    ]