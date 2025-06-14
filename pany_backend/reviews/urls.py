from django.urls import path

from reviews.views import get_reviews


app_name = 'reviews'


urlpatterns = [
    path('', get_reviews, name='reviews')
]