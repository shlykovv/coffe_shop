from django.contrib import admin
from django.utils.safestring import mark_safe

from blog.models import Blog


@admin.register(Blog)
class BlogAdminModel(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'get_image',
        'created_at', 'published'
    )
    fields = (
        'title', 'description', 'image', 'published'
        )
    
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 60px;>')
