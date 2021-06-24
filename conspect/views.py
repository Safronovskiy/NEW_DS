from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import Response, APIView
from .models import *
from .serializers import *




@login_required
def detail_lesson(request, pk=None):
    if pk:
        subjects = StructureComponentModel.objects.filter(subject=pk)
    subjects = StructureComponentModel.objects.filter(subject=pk)
    subj = SubjectModel.objects.all()
    context = {'subjects':subjects, 'subj':subj}
    return render(request, 'index.html', context)

