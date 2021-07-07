from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic
from .forms import *
from django.urls import reverse_lazy


class ConspectCreationView(generic.ListView):
    """ Renders page of conspect compilation """

    template_name = 'index3.html'
    model = SubjectModel
    context_object_name = 'subj'


class ConspectCreationDetailView(generic.DetailView):
    """ Renders page of conspect compilation """

    template_name = 'index3.html'
    model = StructureComponentModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        pk = self.object.pk
        context['subj'] = SubjectModel.objects.all()
        context['subjects'] = StructureComponentModel.objects.filter(subject=pk)
        return context


class ShowSavedConspectsView(generic.ListView):
    """It shows all saved conspect objects on page"""

    template_name = 'saved_conspects.html'
    model = ConspectModel
    context_object_name = 'conspects'
    paginate_by = 8
    ordering = 'date_created'

    def get_queryset(self):

        queryset = ConspectModel.objects.all()
        conspect_name = self.request.GET.get('conspect_name')
        conspect_owner = self.request.GET.get('conspect_owner')
        conspect_date = self.request.GET.get('conspect_date')

        if conspect_name:
            queryset = queryset.filter(name__icontains=conspect_name)
        if conspect_owner:
            queryset = queryset.filter(owner__icontains=conspect_owner)
        if conspect_date:
            queryset = queryset.filter(date_created=conspect_date)

        return queryset



class DetailConspectView(generic.DetailView):
    """It shows detail information about conspect object"""

    model = ConspectModel
    template_name = 'target_consp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        answers = AnswerModel.objects.filter(conspects=pk)
        context['answers'] = answers
        context['components'] = StructureComponentModel.objects.filter(answers__in=answers).distinct()
        return context



class SortByUserConspectView(generic.ListView):

    template_name = 'saved_conspects.html'
    model = ConspectModel
    context_object_name = 'conspects'
    paginate_by = 8
    ordering = ['owner', '-date_created']

    def get_queryset(self):
        return ConspectModel.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):

        if self.__class__.ordering == 'owner':
            self.__class__.ordering = '-owner'
            return redirect('conspect:sort_by_user')

        elif self.__class__.ordering == '-owner':
            self.__class__.ordering = 'owner'
            return redirect('conspect:sort_by_user')



# ---------------- DO NOT FORGET to override this FBV to CBV !!!----------------------


def subject_creation_view(request):
    if request.method == 'POST':
        form = SubjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conspect:detail_lesson')
    form = SubjectForm()
    return render(request, 'creation_form.html', {'form': form})


def structure_component_creation_view(request):
    if request.method == 'POST':
        form = StructureComponentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conspect:detail_lesson')
    form = StructureComponentForm()
    return render(request, 'creation_form.html', {'form': form})


def answer_creation_view(request):
    if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conspect:detail_lesson')
    form = AnswerForm()
    return render(request, 'creation_form.html', {'form': form})
