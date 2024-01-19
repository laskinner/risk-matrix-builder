from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hazard(models.Model):
    name = models.CharField(max_length=100)  # Name of the hazard
    hazard_tag = models.CharField(max_length=30)  # Class/Tag of the hazard
    probability = models.FloatField()  # Probability value of the hazard
    severity = models.IntegerField()  # Numerical metadata for severity
    # Association with Outcome - ForeignKey relationship
    outcome = models.ForeignKey('Outcome', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Outcome(models.Model):
    name = models.CharField(max_length=100)  # Name of the hazard
    probability = models.FloatField()  # Probability value of the hazard
    severity = models.IntegerField()  # Numerical metadata for severity

    def __str__(self):
        return self.name
