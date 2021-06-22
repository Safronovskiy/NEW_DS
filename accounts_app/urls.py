from django.urls import path, include
from .views import *


app_name = 'accounts'

urlpatterns = [

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', user_register_view, name='register'),

]





