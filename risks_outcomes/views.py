from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def risks_outcomes(request):
    return HttpResponse("This will show the risks and outcomes")
