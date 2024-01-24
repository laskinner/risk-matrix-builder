from django.shortcuts import render
from django.views import generic
from .models import Hazard, Outcome 

# Create your views here.

class HazardList(generic.ListView):
    queryset = Hazard.objects.all()
    template_name = "risks_outcomes/hazards_list.html"
    paginate_by = 6

class OutcomeList(generic.ListView):
    queryset = Outcome.objects.all()
    template_name = "risks_outcomes/outcomes_list.html"
    paginate_by = 6
