from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

# Create your views here.
from .models import Snack

class SnackListView(ListView):
  template_name = 'snacks_list.html'
  model = Snack
  context_object_name = 'snacks_list'


class SnackDetailView(DetailView):
  template_name='snack_detail.html'
  model = Snack
  context_object_name = 'snack_object'


class SnackDeleteView(DeleteView):
  template_name = 'snack_delete.html'
  model = Snack
  success_url = reverse_lazy("snacks_list")


class SnackcreateView(CreateView):
  template_name = 'snack_create.html'
  model = Snack
  fields = ['title', 'description', 'purchaser']


class SnackUpdateView(UpdateView):
  template_name = 'snack_update.html'
  model = Snack
  fields = ['title', 'description']

