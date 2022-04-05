from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

 
def Main(request):
    
    return render(request,'home.html')
