from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import *



@login_required
def detail_lesson(request, pk=None):
    subjects = StructureComponentModel.objects.filter(subject=pk)
    subj = SubjectModel.objects.all()
    return render(request, 'index.html', {'subjects':subjects,
                                          'subj':subj})


def show_allconsp_view(request, pk=None):
    if pk:
        answers = AnswerModel.objects.filter(conspects=pk)
        comps = StructureComponentModel.objects.filter(answers__in=answers).distinct()
        return render(request, 'show_consp.html', {'answers': answers,
                                                   'components':comps})

    conspects = ConspectModel.objects.all()
    return render(request, 'show_all.html', {'conspects': conspects})


class ShowAllConspectView(generic.ListView):
    """It shows all conspect objects on page"""

    template_name = 'show_all.html'
    model = ConspectModel
    context_object_name = 'conspects'
    paginate_by = 3


class DetailConspectView(generic.DetailView, LoginRequiredMixin):
    """It shows detail information about conspect object"""

    model = ConspectModel
    template_name = 'show_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        answers = AnswerModel.objects.filter(conspects=pk)
        context['answers'] = answers
        context['components'] = StructureComponentModel.objects.filter(answers__in=answers).distinct()
        return context


class SortByUserConspectView(generic.ListView):
    template_name = 'show_all.html'
    model = ConspectModel
    context_object_name = 'conspects'
    paginate_by = 10


    def get_queryset(self):
        return ConspectModel.objects.filter(owner=self.request.user)


class SortByDateConspectView(generic.ListView):
    template_name = 'show_all.html'
    model = ConspectModel
    context_object_name = 'conspects'
    paginate_by = 5

    # def get_ordering(self):
    #     # ordering = self.request.GET.get('ordering', '-date_created')
    #
    #     if self.get_ordering.ordering:
    #
    #     self.get_ordering.order = ordering
    #     return ordering




def subject_creation_view(request):
    if request.method == 'POST':
        form = SubjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conspect:detail_lesson')
    form = SubjectForm()
    return render(request, 'creation_form.html', {'form':form})


def structure_component_creation_view(request):
    if request.method == 'POST':
        form = StructureComponentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conspect:detail_lesson')
    form = StructureComponentForm()
    return render(request, 'creation_form.html', {'form':form})


def answer_creation_view(request):
    if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conspect:detail_lesson')
    form = AnswerForm()
    return render(request, 'creation_form.html', {'form':form})















