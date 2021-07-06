from django.contrib import admin
from django.urls import path, include




urlpatterns = [

    path('accounts/', include('accounts_app.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('conspect.urls')),

    path('auth/', include('rest_framework.urls')),

]
