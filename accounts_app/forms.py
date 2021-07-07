from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import CustomUserModel




class CustomUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'entrance-login',
                                              'type':'text',
                                              'placeholder':'Имя пользователя',
                                              'required tabindex':'1',
                                              'autocomplete':'off',
                                              'autofocus':'',
                                              }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'entrance-password',
                                                                  'type':'password',
                                                                  'placeholder':'Пароль',
                                                                  'required tabindex':'2',
                                                                  'autocomplete': 'off'}))


class CustomUserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUserModel
        fields = ("username",)









