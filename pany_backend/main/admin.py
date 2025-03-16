from django.contrib import admin
from django.utils.safestring import mark_safe

from main.models import SpecialOffer, OurOffer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_image', 'is_stock')
    readonly_fields = ['get_image']
    
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 60px;>')


@admin.register(SpecialOffer)
class SpecialOfferAdmin(OfferAdmin):
    ...


@admin.register(OurOffer)
class OurOfferAdmin(OfferAdmin):
    ...
