from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('catalog.urls', namespace='catalog')),
    path('', include('main.urls', namespace='main')),
    path('posts/', include('blog.urls', namespace='blog')),
    path('about/', include('about.urls', namespace='about')),
    path('reviews/', include('reviews.urls', namespace='reviews'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
