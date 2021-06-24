from django.urls import path
from .views import *



urlpatterns = [
    path('save_conspect/', save_conspect, name='save'),

]