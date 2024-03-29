from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Product(models.Model):
    RENT = 'rent'
    BUY = 'buy'

    CHOICE_GROUP = {
        (RENT, 'rent'),
        (BUY, 'buy')
    }

    photo = models.ImageField(upload_to="photos", default=None, verbose_name="Фото", null=True)
    name = models.CharField('Название', max_length = 200, null=True)
    description = models.TextField('Описание', null=True)
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, null=True)
    objects = models.Manager()

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуга'

class Comment(models.Model):
    prod = models.ForeignKey(Product, related_name='comments', on_delete = models.PROTECT)
    name = models.ForeignKey(User, on_delete = models.PROTECT)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.name} - {self.prod}"
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'