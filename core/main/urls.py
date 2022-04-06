from django.urls import path
from . import views
from .views import RegisterUser, Main, LoginUser 

 
urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('',  Main.as_view(), name='main'),

]