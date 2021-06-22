from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import CustomUserModel




class CustomUserForm(AuthenticationForm):
    pass


class CustomUserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUserModel
        fields = ("username",)









