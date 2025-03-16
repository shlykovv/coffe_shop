from django.urls import path

from blog.views import get_posts


app_name = 'blog'


urlpatterns = [
    path('', get_posts, name='posts')
]
