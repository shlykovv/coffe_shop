from django.urls import path

from blog.views import get_posts, get_post


app_name = 'blog'


urlpatterns = [
    path('', get_posts, name='posts'),
    path('<int:post_id>/', get_post, name='post')
]
