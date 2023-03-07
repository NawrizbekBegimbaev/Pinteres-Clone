from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField('Пользователь',max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    name = models.CharField('Категория',max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Photo(models.Model):
    title = models.CharField('Название',max_length=1024)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    photo = models.ImageField('Фото',upload_to='upload/')
    nameuser = models.ForeignKey('CustomUser',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'