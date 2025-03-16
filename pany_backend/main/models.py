from django.db import models


class SpecialOffer(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='offer/special/')
    is_stock = models.BooleanField(default=True)


class OurOffer(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='offer/our_offer/')
    is_stock = models.BooleanField(default=True)
