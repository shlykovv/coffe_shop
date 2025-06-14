from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    photo = models.ImageField(blank=True, null=True, upload_to='media/users/')
    client = models.CharField(max_length=100, verbose_name='Клиент')
    stars = models.DecimalField(verbose_name='Рейтинг', max_digits=2, decimal_places=1)
    content = models.TextField(verbose_name='Отзыв')
