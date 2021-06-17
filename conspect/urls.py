from django.urls import path
from django.views.generic import TemplateView

from .views import LessonView, lessons

app_name = 'conspect'


urlpatterns = [
    # path('', LessonView.as_view(), name='lessons'),
    path('', TemplateView.as_view(template_name='home_page.html'), name='home'),
    path('conspect/', lessons, name='lessons_tmp'),
]