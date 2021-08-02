from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, FormView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .forms import *




class StartPageView(TemplateView):

    template_name = 'home_page2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        footer = FooterInfoModel.objects.all().first()
        context['info'] = footer
        return context


class ConspectCreationView(ListView):

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


class ShowSavedConspectsView(ListView):

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


class DetailConspectView(DetailView):

    model = ConspectModel
    template_name = 'target_consp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        answers = AnswerModel.objects.filter(conspects=pk)
        context['answers'] = answers
        context['components'] = StructureComponentModel.objects.filter(answers__in=answers).distinct()
        return context


class MethodistDesktopView(LoginRequiredMixin, ListView):

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


class EditSubjectView(LoginRequiredMixin, UpdateView):
    template_name = 'subject_edit_object.html'
    model = SubjectModel
    form_class = SubjectForm
    success_url = reverse_lazy('conspect:methodist_desktop')

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = SubjectModel.objects.filter(id=pk)
        return queryset


class EditComponentView(LoginRequiredMixin, UpdateView):
    template_name = 'structure_edit_object.html'
    model = StructureComponentModel
    form_class = StructureComponentForm
    success_url = reverse_lazy('conspect:methodist_desktop')

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = StructureComponentModel.objects.filter(id=pk)
        return queryset


class EditAnswerView(LoginRequiredMixin, UpdateView):
    template_name = 'answer_edit_object.html'
    model = AnswerModel
    form_class = AnswerForm
    success_url = reverse_lazy('conspect:methodist_desktop')

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = AnswerModel.objects.filter(id=pk)
        return queryset


class SubjectCreationView(LoginRequiredMixin, FormView):
    template_name = 'subject_creation_form.html'
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
    template_name = 'structure_creation_form.html'
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
    template_name = 'answer_creation_form.html'
    form_class = AnswerForm
    success_message = 'Объект успешно создан!'
    success_url = reverse_lazy('conspect:answ_creation')

    def get_initial(self):
        initial = {'author': self.request.user}
        return initial

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class EditConspectView(LoginRequiredMixin, UpdateView):
    template_name = 'edit_conspect.html'
    model = ConspectModel
    fields = ['name', 'answers']
    success_url = reverse_lazy('conspect:show_details')




