from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class schoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class schoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'class_based_views_application/school_details.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("class_based_views_application:list")
