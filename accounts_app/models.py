from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models



class CustomUserManager(UserManager):
    pass


class CustomUserModel(AbstractUser):
    is_methodist = models.BooleanField(default=False, help_text='Отметьте, если пользователь является преподавателем.',
                                       verbose_name='Статус методиста')
    is_teacher = models.BooleanField(default=False, help_text='Отметьте, если пользователь является методистом.',
                                     verbose_name='Статус преподавателя')

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return f'{self.username}'














