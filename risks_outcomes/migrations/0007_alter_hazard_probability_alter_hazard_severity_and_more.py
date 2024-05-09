# Generated by Django 4.2 on 2024-05-08 15:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risks_outcomes', '0006_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hazard',
            name='probability',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='hazard',
            name='severity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='probability',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='severity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]