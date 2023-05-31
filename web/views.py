from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.db.models import Min, Max
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import UserModel, ProjectsModel, CollectionsModel, ContactUSModel, LogoModel
from .forms import LoginForm, RegistrationForm, ContactModelForm

class Logo(TemplateView):
    template_name = "layouts/header.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['logos'] = LogoModel.objects.all()[:1]
        return data

class main(TemplateView):
    template_name = "pages/main.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['projects'] = ProjectsModel.objects.all()[:9]
        data['logos'] = LogoModel.objects.all()[:1]
        return data


class about(TemplateView):
    template_name = "pages/about.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['logos'] = LogoModel.objects.all()[:1]
        return data

class projects(ListView):
    model = ProjectsModel
    template_name = "pages/projects.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['logos'] = LogoModel.objects.all()[:1]
        return data

class collections(ListView):
    model = CollectionsModel
    template_name = "pages/collections.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['logos'] = LogoModel.objects.all()[:1]
        return data

class detailprojects(DetailView):
    model = ProjectsModel
    template_name = "pages/detailprojects.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['logos'] = LogoModel.objects.all()[:1]
        return data

class detailcollections(DetailView):
    model = CollectionsModel
    template_name = "pages/detailcollections.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['logos'] = LogoModel.objects.all()[:1]
        return data

class contactus(CreateView):
    form_class = ContactModelForm
    template_name = 'pages/contact.html'

    def get_success_url(self):
        return reverse('contact')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(contactus, self).form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['contact'] = ContactUSModel.objects.all().filter(user=self.request.user)
        data['contact_admin'] = ContactUSModel.objects.all()
        data['logos'] = LogoModel.objects.all()[:1]
        return data
    
class contactdetail(DetailView):
    model = ContactUSModel
    template_name = "pages/contactdetail.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['logos'] = LogoModel.objects.all()[:1]
        return data

def adminPanel(request):
    if request.user.is_staff:
        template_name = 'pages/admin.html'
        model = ContactUSModel.objects.all()
        logo = LogoModel.objects.all()[:1]
        return render(request, template_name, context={
            'contact_list': model,
            'logos': logo
        })
    else:
        return redirect('main')

# Registration View
def signup(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('main')
    else:
        template_name = 'pages/signup.html'
        form_registration = RegistrationForm()
        if request.method == 'POST':
            form_registration = RegistrationForm(data=request.POST, files=request.FILES)
            if form_registration.is_valid():
                del form_registration.cleaned_data['confirm_password']
                user_registration = UserModel(
                    username=form_registration.cleaned_data['username'],
                    password=make_password(form_registration.cleaned_data['password']),
                    email=form_registration.cleaned_data['email']
                )
                user_registration.save()
                return redirect('signin')
            # raise ValidationError(form_registration.errors)

        return render(request, template_name, context={
            'form': form_registration
        })

# --------------------------------------------------------------------------- #
# Login View
def signin(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('main')
    else:
        template_name = 'pages/signin.html'
        form_login = LoginForm()
        if request.method == 'POST':
            form_login = LoginForm(data=request.POST)
            if form_login.is_valid():
                user_login = authenticate(
                    username=form_login.cleaned_data['username'],
                    password=form_login.cleaned_data['password']
                )
                if user_login is not None:
                    login(request, user_login)
                    return redirect('main')
                form_login.add_error('password', 'Username or password is incorrect')

        return render(request, template_name, context={
            'form': form_login
        })

def logoutView(request):
    logout(request)
    return redirect('main')