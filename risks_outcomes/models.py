from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Hazard(models.Model):
    # Existing fields
    name = models.CharField(max_length=100)
    hazard_tag = models.CharField(max_length=30)
    probability = models.FloatField()
    severity = models.IntegerField()
    outcome = models.ForeignKey('Outcome', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hazard_author")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)
    supporting_documents = CloudinaryField('document', default='placeholder')  # Assuming Cloudinary setup

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="outcome_author")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)
    supporting_documents = CloudinaryField('document', default='placeholder')  # Assuming Cloudinary setup

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Comment(models.Model):
    hazard = models.ForeignKey(Hazard, on_delete=models.CASCADE, related_name="hazard_comments", null=True, blank=True)
    outcome = models.ForeignKey(Outcome, on_delete=models.CASCADE, related_name="outcome_comments", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

class Document(models.Model):
    file = CloudinaryField('document')
    hazard = models.ForeignKey(Hazard, related_name='documents', on_delete=models.CASCADE, null=True, blank=True)
    outcome = models.ForeignKey(Outcome, related_name='documents', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Document for {self.hazard.name if self.hazard else self.outcome.name}"
