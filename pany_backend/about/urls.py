from django.urls import path

from about.views import get_about


app_name = 'about'


urlpatterns = [
    path('', get_about, name='about')
]

