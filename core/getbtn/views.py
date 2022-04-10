from django.shortcuts import render
from .models import GetBtn
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from django.views import generic



def GetBtnView(request):
    dataset=GetBtn.objects.filter()
    if request.user.is_authenticated == True:
        template = 'getbtn/auth.html'
        return render(
        request,
        'getbtn/getbtn.html',
        context={'dataset':template}
        )
    else:

   
        template = 'getbtn/noauth.html'
        return render(
        request,
        'getbtn/getbtn.html',
        context={'dataset':template}
        )
