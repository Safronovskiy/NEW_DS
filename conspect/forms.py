from django import forms
from .models import *




class SubjectForm(forms.ModelForm):
    name = forms.CharField(label='Название предмета', widget=forms.Textarea(attrs={'class': 'input', 'rows':1}))

    class Meta:
        model = SubjectModel
        fields ='__all__'
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden', 'class': '_input'}),
        }


class StructureComponentForm(forms.ModelForm):

    class Meta:
        model = StructureComponentModel
        fields = '__all__'
        widgets = {
            'author': forms.HiddenInput(attrs={'class': '_input'}),
            'subject': forms.Select(attrs={'class': 'subject_input'}),
            'name': forms.Textarea(attrs={'class': 'input', 'rows':1}),
        }


class AnswerForm(forms.ModelForm):

    class Meta:
        model = AnswerModel
        fields = '__all__'
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden', 'class': 'answer_input'}),
            'structure_component': forms.Select(attrs={'class': '_input'}),
            'content': forms.Textarea(attrs={'class': 'input'})
        }


class ConspectForm(forms.ModelForm):

    class Meta:
        model = ConspectModel
        fields = '__all__'
