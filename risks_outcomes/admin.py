from django.contrib import admin
from .models import Hazard, Outcome, Comment

# Register your models here.
admin.site.register(Hazard)
admin.site.register(Outcome)
admin.site.register(Comment)
