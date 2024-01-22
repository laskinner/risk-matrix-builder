from django.shortcuts import render
from django.views import generic
from .models import Hazard 

# Create your views here.

class HazardList(generic.ListView):
    queryset = Hazard.objects.all()
    template_name = "hazards_list.html"
