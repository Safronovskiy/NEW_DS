from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'conspect'


urlpatterns = [
    path('', TemplateView.as_view(template_name='home_page2.html'), name='home'),

    path('conspect_creation/', ConspectCreationView.as_view(), name='conspect_creation'),
    path('conspect_creation/<int:pk>', ConspectCreationDetailView.as_view(), name='conspect_creation'),
    path('show_all/', ShowSavedConspectsView.as_view(), name='show_all'),
    path('show_details/<int:pk>/', DetailConspectView.as_view(), name='show_details'),
    path('show_all/sort_by_user/', SortByUserConspectView.as_view(), name='sort_by_user'),
    path('delete_conspect/<int:pk>/', DeleteConspectView.as_view(), name='delete_conspect'),


    # --------------  FBV with form for objects creation---------------
    path('subj_creation/', subject_creation_view, name='subj_creation'),
    path('component_creation/', structure_component_creation_view, name='comp_creation'),
    path('answer_creation/', answer_creation_view, name='answ_creation'),


# -------------------- endpoints for FBV (delete)------------------------------
#     path('conspect/', detail_lesson, name='detail_lesson'),
#     path('conspect/<int:pk>', detail_lesson, name='detail_lesson'),
#path('show_conspects/', show_allconsp_view, name='show_all'),
#path('show_conspect/<int:pk>/', show_allconsp_view, name='show_details'),
]