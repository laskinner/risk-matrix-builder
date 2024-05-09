from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import CommentForm
from .models import Hazard, Outcome, Comment

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
    hazard = get_object_or_404(Hazard, slug=slug)
    comments = (
        hazard.hazard_comments.filter(approved=True).order_by("-created_on")
    )
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.hazard = hazard
            comment.save()
            messages.success(request, "Comment submitted and awaiting approval")
            return redirect(
                "hazard_detail", slug=slug
            )  # Redirect to avoid resubmission
    else:
        comment_form = CommentForm()

    context = {
        "hazard": hazard,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }
    return render(request, "risks_outcomes/hazard_detail.html", context)


def outcome_detail(request, slug):
    """
    Display an individual :model:`risks_outcomes.Outcome`.

    **Context**

    ``outcome``
        An instance of :model:`risks_outcomes.Outcome`.

    **Template:**

    :template:`risks_outcomes/outcome_detail.html`
    """

    outcome = get_object_or_404(Outcome, slug=slug)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.outcome = outcome
            comment.save()
            messages.success(
                request, "Comment submitted and awaiting admin approval"
            )
            return redirect("outcome_detail", slug=slug)  # Redirect to the same page
    else:
        comment_form = CommentForm()

    comments = (
        outcome.outcome_comments.filter(approved=True).order_by("-created_on")
    )
    comment_count = comments.count()

    context = {
        "outcome": outcome,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }
    return render(request, "risks_outcomes/outcome_detail.html", context)


def comment_edit(request, slug, comment_id, comment_type):
    """
    View to edit comments for either Hazard or Outcome.
    """
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Comment updated and awaiting admin approval!",
            )

            if comment_type == "hazard":
                hazard = get_object_or_404(Hazard, slug=slug)
                return HttpResponseRedirect(
                    reverse("hazard_detail", args=[slug])
                )
            elif comment_type == "outcome":
                outcome = get_object_or_404(Outcome, slug=slug)
                return HttpResponseRedirect(
                    reverse("outcome_detail", args=[slug])
                )
        else:
            messages.add_message(
                request, messages.ERROR, "Error updating comment!"
            )

    # Redirect to the appropriate detail page based on comment_type
    if comment_type == "hazard":
        return HttpResponseRedirect(reverse(
            "hazard_detail", args=[slug])
                                   )
    elif comment_type == "outcome":
        return HttpResponseRedirect(
            reverse("outcome_detail", args=[slug])
        )

    # Redirect to home if comment_type is not recognized
    return redirect("home")


def hazard_comment_delete(request, slug, comment_id):
    """
    View to delete a comment related to a Hazard.
    """
    hazard = get_object_or_404(Hazard, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, hazard=hazard)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, "Comment deleted!"
        )
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("hazard_detail", args=[slug]))


def outcome_comment_delete(request, slug, comment_id):
    """
    View to delete a comment related to an Outcome.
    """
    outcome = get_object_or_404(Outcome, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, outcome=outcome)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("outcome_detail", args=[slug]))
