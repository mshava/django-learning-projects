from django.shortcuts import render
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

class createSchoolView(CreateView):
    context_object_name = 'schoolCreate'
