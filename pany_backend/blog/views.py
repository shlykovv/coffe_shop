from django.shortcuts import render

from blog.models import Blog


def get_posts(request):
    posts = Blog.objects.filter(published=True)
    context = {
        'posts': posts
    }
    return render(request, 'blog/posts.html', context)


def get_post(request, post_id: int):
    post = Blog.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)
