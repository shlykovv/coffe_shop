from django.shortcuts import render

from catalog.models import Product


def get_products(request):
    products = Product.objects.all()
    title = 'Наше меню'
    context = {
        'products': products,
        'title': title
    }
    return render(request, 'catalog/products.html', context=context)


def get_contacts(request):
    return render(request, 'catalog/contacts.html')
