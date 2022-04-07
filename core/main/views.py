from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .utils import *
from .forms import *
from blog.models import Category, News
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q

class Main(ListView):
    model = Category
    template_name = 'home.html'


def logout_user(request):
    logout(request)
    return redirect('main')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))



class SearchResultsView(ListView):
    model = News
    template_name = 'search.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        try:
            object_list = News.objects.filter(
              Q(h1__icontains=query) | Q(title__icontains=query) | Q(post__icontains=query)
             )
        except:
            object_list=""
        return object_list