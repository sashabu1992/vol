from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .utils import *
from .forms import *
from blog.models import Category

from django.urls import reverse, reverse_lazy



class Main(ListView):
    model = Category
    template_name = 'home.html'



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    
    def logout_user(request):
        logout(request)
        return redirect('login')
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
