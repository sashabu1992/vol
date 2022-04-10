from django.urls import path, re_path
from . import views
from .views import GetBtnView


urlpatterns = [
    path('',  views.GetBtnView, name='getbtn'),   
]