from django.urls import path

from reviews.views import get_reviews, set_review


app_name = "reviews"


urlpatterns = [
    path("", get_reviews, name="reviews"),
    path("add/", set_review, name="set_review"),
]
