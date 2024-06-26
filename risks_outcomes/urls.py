from django.urls import path
from . import views

urlpatterns = [
    path("", views.HazardList.as_view(), name="hazards"),
    path("outcomes/", views.OutcomeList.as_view(), name="outcomes"),
    path("hazards/<slug:slug>/", views.hazard_detail, name="hazard_detail"),
    path("outcomes/<slug:slug>/", views.outcome_detail, name="outcome_detail"),
    path(
        "<str:comment_type>/<slug:slug>/comment/<int:comment_id>/edit/",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "hazards/<slug:slug>/hazard/comments/<int:comment_id>/delete/",
        views.hazard_comment_delete,
        name="hazard_comment_delete",
    ),
    path(
        "outcomes/<slug:slug>/outcome/comments/<int:comment_id>/delete/",
        views.outcome_comment_delete,
        name="outcome_comment_delete",
    ),
]
