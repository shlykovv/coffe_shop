from django.shortcuts import render

from blog.models import Blog


def get_posts(request):
    posts = Blog.objects.filter(published=True)
    context = {
        'posts': posts
    }
    return render(request, 'blog/posts.html', context)
