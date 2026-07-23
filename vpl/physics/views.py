from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class HomeSimView(TemplateView):
    template_name = 'physics/index.html'
    