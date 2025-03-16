from django.urls import path

from main.views import get_home_page

app_name = 'main'


urlpatterns = [
    path('', get_home_page, name='home')
]