from django.shortcuts import render


def get_about(request):
    context = {
        'title': 'about us'
    }
    return render(request, 'about/about.html', context)
