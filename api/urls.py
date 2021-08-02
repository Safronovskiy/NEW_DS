from django.urls import path
from .views import *



urlpatterns = [

    path('conspect/all/', GetAllConspectsView.as_view(), name='api_get_all'),
    path('conspect/<int:pk>/', DetailConspectView.as_view(), name='api_get_conspect'),
    path('conspect/create/', CreateConspectView.as_view(), name='api_create_conspect'),


]








