from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'conspect'


urlpatterns = [

    path('', TemplateView.as_view(template_name='home_page.html'), name='home'),
    path('conspect/', detail_lesson, name='detail_lesson'),
    path('conspect/<int:pk>', detail_lesson, name='detail_lesson'),
    path('subj_creation/', subject_creation_view, name='subj_creation'),
    path('component_creation/', structure_component_creation_view, name='comp_creation'),
    path('answer_creation/', answer_creation_view, name='answ_creation'),
    path('show_conspects/', show_allconsp_view, name='show_all'),
    path('show_conspect/<int:pk>/', show_allconsp_view, name='show_consp'),


]