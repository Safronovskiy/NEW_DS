from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import Response, APIView
from .models import *
from .serializers import *
from .forms import *



@login_required
def detail_lesson(request, pk=None):
    subjects = StructureComponentModel.objects.filter(subject=pk)
    subj = SubjectModel.objects.all()
    return render(request, 'index.html', {'subjects':subjects,
                                          'subj':subj})



def show_allconsp_view(request, pk=None):
    if pk:
        conspect = get_object_or_404(ConspectModel, pk=pk)

        return render(request, 'show_consp.html', {'conspect': conspect,
                                                   'components':components})

    conspects = ConspectModel.objects.all()
    return render(request, 'show_all.html', {'conspects': conspects})















def subject_creation_view(request):
    if request.method == 'POST':
        form = SubjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conspect:subj_creation')
    form = SubjectForm()
    return render(request, 'creation_form.html', {'form':form})


def structure_component_creation_view(request):
    if request.method == 'POST':
        form = StructureComponentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conspect:subj_creation')
    form = StructureComponentForm()
    return render(request, 'creation_form.html', {'form':form})


def answer_creation_view(request):
    if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conspect:subj_creation')
    form = AnswerForm()
    return render(request, 'creation_form.html', {'form':form})















