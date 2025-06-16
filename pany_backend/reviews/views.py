from django.shortcuts import render
from django.urls import reverse

from reviews.models import Review
from reviews.forms import ReviewForm


def get_reviews(request):
    reviews = Review.objects.all()
    context = {"title": "Coffe - Отзывы", "reviews": reviews}
    return render(request, "reviews/review.html", context=context)


def set_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return reverse("reviews:reviews")
    else:
        form = ReviewForm()

    context = {"form": form}
    return render(request, "reviews/add_review.html", context=context)
