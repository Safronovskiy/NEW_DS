from django import forms
from .models import *




class SubjectForm(forms.ModelForm):

    class Meta:
        model = SubjectModel
        fields ='__all__'
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden'})
        }



class StructureComponentForm(forms.ModelForm):

    class Meta:
        model = StructureComponentModel
        fields = '__all__'
        widgets = {
            'author': forms.HiddenInput()
        }

class AnswerForm(forms.ModelForm):

    class Meta:
        model = AnswerModel
        fields = '__all__'
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden'})
        }


class ConspectForm(forms.ModelForm):

    class Meta:
        model = ConspectModel
        fields = '__all__'
