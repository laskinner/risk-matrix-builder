# Generated by Django 4.2.8 on 2024-01-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risks_outcomes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hazard',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]