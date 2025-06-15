from django.shortcuts import render

from reviews.models import Review


def get_reviews(request):
    reviews = Review.objects.all()
    context = {
        'title': 'Coffe - Отзывы',
        'reviews': reviews
    }
    return render(request, 'reviews/review.html', context=context)

