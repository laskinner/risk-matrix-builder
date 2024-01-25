from django.shortcuts import render, get_object_or_404
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

def hazard_detail(request, slug):
    """
    Display an individual :model:`risks_outcomes.Hazard`.

    **Context**

    ``hazard``
        An instance of :model:`risks_outcomes.Hazard`.

    **Template:**

    :template:`risks_outcomes/hazard_detail.html`
    """

    queryset = Hazard.objects.all()
    hazard = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "risks_outcomes/hazard_detail.html",
        {"hazard": hazard},
    )

def outcome_detail(request, slug):
    """
    Display an individual :model:`risks_outcomes.Outcome`.

    **Context**

    ``outcome``
        An instance of :model:`risks_outcomes.Outcome`.

    **Template:**

    :template:`risks_outcomes/outcome_detail.html`
    """

    queryset = Outcome.objects.all()
    outcome = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "risks_outcomes/outcome_detail.html",
        {"outcome": outcome},
    )
