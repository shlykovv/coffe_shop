from django.urls import path

from catalog.views import get_products, get_contacts

app_name = 'catalog'


urlpatterns = [
    path('', get_products, name='products'),
    path('contacts/', get_contacts, name='contacts')
]