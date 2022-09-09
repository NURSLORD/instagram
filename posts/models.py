from django.db import models

from account.models import User


# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Имя пользователя', related_name='posts')
    image = models.ImageField(verbose_name="Фото", upload_to="Post/Y%/%m/%d")
    description = models.TextField(verbose_name='Описание')
    is_posted = models.DateTimeField(verbose_name='Опубликовано', auto_now_add=True)

    def __str__(self):
        return f'{self.owner}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


