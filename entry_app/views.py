from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ModelApp
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


def hello_world(request):
    return HttpResponse('<h2>hello ザ　わーるど！ フロムapp</h2>')

def world(request):
    return HttpResponse('<h2>World! フロムapp</h2>')

class ListEntryView(ListView):
    template_name = 'entry/entry_model_list.html'
    model = ModelApp

class DetailEntryView(LoginRequiredMixin, DetailView):
    template_name = 'entry/entry_model_detail.html'
    model = ModelApp

class CreateEntryView(LoginRequiredMixin, CreateView):
    template_name = 'entry/entry_create.html'
    model = ModelApp
    fields = ['t_title', 't_text']
    success_url = reverse_lazy('list_entry')

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.user = self.request.user
        entry.save()
        return super().form_valid(form)

class UserView(LoginRequiredMixin,ListView):
    template_name = 'entry/entry_model_list.html'
    paginate_by = 9

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = ModelApp.objects.filter(user=user_id)
        return user_list

class UpdateEntryView(LoginRequiredMixin, UpdateView):
    template_name = 'entry/entry_update.html'
    model = ModelApp
    fields = ['t_title', 't_text']
    success_url = reverse_lazy('list_entry')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

class DeleteEntryView(LoginRequiredMixin, DeleteView):
    template_name = 'entry/entry_delete.html'
    model = ModelApp
    success_url = reverse_lazy('list_entry')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj