from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel
from .forms import CustomUserRegisterForm



@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserRegisterForm
    list_display = ('username', 'is_methodist', 'is_teacher', 'first_name', 'last_name')
    list_editable = ('is_methodist', 'is_teacher', 'first_name', 'last_name')
    fieldsets = (
        ('Логин и пароль', {'fields': ('username', 'password')}),
        (('Персональная информация'), {'fields': ('first_name', 'last_name',)}),
        (('Права доступа'), {
            'fields': ('is_active', 'is_teacher', 'is_methodist','is_staff', 'is_superuser')
        }),
        (('Даты последнего посещения и регистрации пользователя'), {'fields': ('last_login', 'date_joined')}),
    )

    list_filter = ('is_methodist', 'is_teacher','is_active')













