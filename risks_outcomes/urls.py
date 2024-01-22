from django.urls import path
from . import views

urlpatterns = [
    path('', views.HazardList.as_view(), name='home'),
]
