from django import forms
from .models import *




class SubjectForm(forms.ModelForm):

    class Meta:
        model = SubjectModel
        fields ='__all__'


class StructureComponentForm(forms.ModelForm):
    class Meta:
        model = StructureComponentModel
        fields = '__all__'


class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerModel
        fields = '__all__'


