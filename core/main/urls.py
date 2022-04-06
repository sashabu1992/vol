from django.urls import path
from . import views
from .views import RegisterUser, Main 

 
urlpatterns = [
    #path('register/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('',  Main.as_view(), name='main'),

]