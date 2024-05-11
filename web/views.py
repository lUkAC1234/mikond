from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

class main(TemplateView):
    template_name = "pages/main.html"