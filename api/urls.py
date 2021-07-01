from django.urls import path
from .views import *



urlpatterns = [
    path('save_conspect/', save_conspect, name='save'),
    path('get_conspects/', GetAllConspectsView.as_view(), name='api_get_all'),
    path('get_conspects/<int:pk>/', DetailConspectView.as_view(), name='api_get_conspect'),
    path('create_conspect/', CreateConspectView.as_view(), name='api_create_conspect'),
]








