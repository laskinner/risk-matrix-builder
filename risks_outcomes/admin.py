from django.contrib import admin
from .models import Hazard, Outcome

# Register your models here.
admin.site.register(Hazard)
admin.site.register(Outcome)
