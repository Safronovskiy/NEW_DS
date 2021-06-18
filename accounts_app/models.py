from django.contrib.auth.models import AbstractUser
from django.db import models




class CustomUserModel(AbstractUser):
    is_methodist = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)





















