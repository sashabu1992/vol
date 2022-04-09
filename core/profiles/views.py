from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, Http404, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import UserProfileForm


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
    


class EditProfileView(UpdateView):
    # Модель куда выполняется сохранение
    model = Profile
    # Класс на основе которого будет валидация полей
    form_class = UserProfileForm
    # Выведем все существующие записи на странице
    extra_context = {'profile': Profile.objects.all()}
    # Шаблон с помощью которого
    # будут выводиться данные
    template_name = 'editprofile.html'
    # На какую страницу будет перенаправление
    # в случае успешного сохранения формы
 
    def get_success_url(self):
        return reverse('profile_link', kwargs={'pk': self.request.user.pk})


 