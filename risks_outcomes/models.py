from django.db import models
from django.template.defaultfilters import slugify

class Hazard(models.Model):
    name = models.CharField(max_length=100)
    hazard_tag = models.CharField(max_length=30)
    probability = models.FloatField()
    severity = models.IntegerField()
    outcome = models.ForeignKey('Outcome', on_delete=models.SET_NULL,
                                null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Outcome(models.Model):
    name = models.CharField(max_length=100)
    probability = models.FloatField()
    severity = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
