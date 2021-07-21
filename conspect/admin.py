from django.contrib import admin
from .models import *
from .forms import *




@admin.register(SubjectModel)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')


@admin.register(StructureComponentModel)
class StructureComponentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'author')


@admin.register(AnswerModel)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('content', 'structure_component',  'author')


@admin.register(ConspectModel)
class ConspectModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',  'date_created')


@admin.register(FooterInfoModel)
class FooterInfoModelAdmin(admin.ModelAdmin):
    # list_display = ('requisites', 'contacts', 'about')
    # list_editable = ('requisites', 'contacts', 'about')
    # list_display_links = ()
    pass


