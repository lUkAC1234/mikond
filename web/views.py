from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import ContactModel, ServiceOption, ServiceModel, OurWorksModel
from .forms import ContactModelForm
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound, Http404

class main(CreateView):
    template_name = "pages/main.html"
    model = ContactModel
    form_class = ContactModelForm
    success_url = reverse_lazy('main:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_options'] = ServiceOption.objects.all()
        context['service_first'] = ServiceModel.objects.first()
        context['services'] = ServiceModel.objects.all()[:4]
        return context
        
    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
    
class catalogView(CreateView):
    template_name = "pages/catalog.html"
    model = ContactModel
    form_class = ContactModelForm
    success_url = reverse_lazy('main:catalog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_options'] = ServiceOption.objects.all()
        context['services'] = ServiceModel.objects.all()
        return context
    
    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class serviceDetailView(DetailView):
    template_name = "pages/service.html"
    model = ServiceModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.all()[:4]
        return context
    
class ourWorksView(CreateView):
    template_name = "pages/ourworks.html"
    model = ContactModel
    form_class = ContactModelForm
    success_url = reverse_lazy('main:ourworks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_options'] = ServiceOption.objects.all()
        context['our_works'] = OurWorksModel.objects.all()
        return context
    
    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
    
def PageNotFound(request, *args, **kwargs):
    text = render_to_string('pages/page404.html')
    return HttpResponseNotFound(text)