from django.shortcuts import render

from main.models import SpecialOffer, OurOffer


def get_home_page(request):
    special_offer = SpecialOffer.objects.filter(is_stock=True)
    offers = OurOffer.objects.filter(is_stock=True)
    context = {
        'special_offer': special_offer,
        'offers': offers
    }
    return render(request, 'main/main.html', context)
