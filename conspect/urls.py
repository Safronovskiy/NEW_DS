from django.urls import path
from .views import *

app_name = 'conspect'


urlpatterns = [

    path('', StartPageView.as_view(), name='home'),

    path('conspect_creation/<int:pk>', ConspectCreationView.as_view(), name='conspect_creation'),
    path('conspect_creation/', ConspectCreationView.as_view(), name='conspect_creation'),

    path('show_all/', ShowSavedConspectsView.as_view(), name='show_all'),
    path('show_details/<int:pk>/', DetailConspectView.as_view(), name='show_details'),
    path('methodist_desktop/', MethodistDesktopView.as_view(), name='methodist_desktop'),
    path('methodist_desktop/subject_creation/', SubjectCreationView.as_view(), name='subj_creation'),
    path('methodist_desktop/component_creation/', StructureComponentCreationView.as_view(), name='comp_creation'),
    path('methodist_desktop/answer_creation/', AnswerCreationView.as_view(), name='answ_creation'),

    path('edit_subject/<int:pk>/', EditSubjectView.as_view(), name='edit_subj'),
    path('edit_component/<int:pk>/', EditComponentView.as_view(), name='edit_comp'),
    path('edit_answer/<int:pk>/', EditAnswerView.as_view(), name='edit_answ'),
    path('edit_conspect/<int:pk>', EditConspectView.as_view(), name='edit_conspect'),

]