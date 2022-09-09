from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользовател'
        verbose_name_plural = 'Пользователи'

    image = models.ImageField(verbose_name='Фото', upload_to='Customers/%Y/%m/%d', default='Customers/2022/09/09/default-avatar-profile-icon-vector-social-media-user-photo-18304237_NLdrISN.jpg')
    phone = models.CharField(verbose_name='Номер', max_length=80, null=True, blank=True)
    biography = models.TextField(verbose_name='Биография', null=True, blank=True)
    def __str__(self):
        return f'{self.username}'