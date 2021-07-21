from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import FormView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages



class StartPageView(TemplateView):
    template_name = 'home_page2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        footer = FooterInfoModel.objects.get(id=1)
        context['info'] = footer
        return context


class ConspectCreationView(generic.ListView):
    """ Renders page of conspect compilation """

    template_name = 'index3.html'
    model = SubjectModel
    context_object_name = 'subj'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('pk'):
            pk = self.kwargs.get('pk')
            context['subj'] = SubjectModel.objects.all()
            context['subjects'] = StructureComponentModel.objects.filter(subject=pk)
            return context
        return context


# class ConspectCreationDetailView(generic.DetailView):
#     """ Renders page of conspect compilation """
#
#     template_name = 'index3.html'
#     model = StructureComponentModel
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         self.object = self.get_object()
#         pk = self.object.pk
#         context['subj'] = SubjectModel.objects.all()
#         context['subjects'] = StructureComponentModel.objects.filter(subject=pk)
#         return context



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

        if conspect_name:
            queryset = queryset.filter(name__icontains=conspect_name)
        if conspect_owner:
            queryset = queryset.filter(owner__icontains=conspect_owner)
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



class MethodistDesktopView(generic.ListView, LoginRequiredMixin):

    template_name = 'methodist_desktop.html'
    model = SubjectModel
    context_object_name = 'subj'
    success_message = 'Объект успешно создан'

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        user = self.request.user
        content['my_subjects'] = SubjectModel.objects.filter(author=user)
        content['my_components'] = StructureComponentModel.objects.filter(author=user)
        content['my_answers'] = AnswerModel.objects.filter(author=user)
        return content


class EditSubjectView(UpdateView):
    template_name = 'edit_object.html'
    model = SubjectModel
    fields = ['name']
    success_url = reverse_lazy('conspect:methodist_desktop')

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = SubjectModel.objects.filter(id=pk)
        return queryset


class EditComponentView(UpdateView):
    template_name = 'edit_object.html'
    model = StructureComponentModel
    fields = ['name', 'subject']
    success_url = reverse_lazy('conspect:methodist_desktop')

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = StructureComponentModel.objects.filter(id=pk)
        return queryset


class EditAnswerView(UpdateView):
    template_name = 'edit_object.html'
    model = AnswerModel
    fields = ['content', 'structure_component']
    success_url = reverse_lazy('conspect:methodist_desktop')

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = AnswerModel.objects.filter(id=pk)
        return queryset







class SubjectCreationView(LoginRequiredMixin, FormView):
    template_name = 'creation_form.html'
    form_class = SubjectForm
    success_message = 'Объект успешно создан!'
    success_url = reverse_lazy('conspect:subj_creation')

    def get_initial(self):
        initial = {'author': self.request.user}
        return initial

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

class StructureComponentCreationView(LoginRequiredMixin, FormView):
    template_name = 'creation_form.html'
    form_class = StructureComponentForm
    success_message = 'Объект успешно создан!'
    success_url = reverse_lazy('conspect:comp_creation')

    def get_initial(self):
        initial = {'author': self.request.user}
        return initial

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

class AnswerCreationView(LoginRequiredMixin,FormView):
    template_name = 'creation_form.html'
    form_class = AnswerForm
    success_message = 'Объект успешно создан!'
    success_url = reverse_lazy('conspect:answ_creation')

    def get_initial(self):
        initial = {'author': self.request.user}
        return initial

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)








# ---------------- DO NOT FORGET to override this FBV to CBV !!!----------------------


def subject_creation_view(request):
    if request.method == 'POST':
        form = SubjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            message = messages.success(request, f'Предмет {form.cleaned_data.get("name")} успешно создан')
            return render(request, 'creation_form.html', {'form': form, 'messages':message,})
    form = SubjectForm(initial={'author': request.user})
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




def edit_conspectview(request):
    id = request.GET.get('id')[-3:-1]
    print(id)
    consp = ConspectModel.objects.get(id=id)
    form = ConspectForm(instance=consp)
    return render(request, 'edit_conspect.html', {'form': form})

