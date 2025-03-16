from django.contrib import admin
from django.utils.safestring import mark_safe

from catalog.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'image',
              'price', 'sale', 'in_stock')
    readonly_fields = ['get_image']
    
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;>')
