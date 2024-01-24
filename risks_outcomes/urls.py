from django.urls import path
from . import views

urlpatterns = [
    path('', views.HazardList.as_view(), name='hazards'),
    path('outcomes', views.OutcomeList.as_view(), name='outcomes'),
    # path('<slug:slug>/', views.hazard_detail, name='hazard_detail'),
    # path('<slug:slug>/', views.outcome_detail, name='outcome_detail'),
]
