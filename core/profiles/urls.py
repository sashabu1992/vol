from django.urls import path, re_path
from . import views
from .views import ShowProfilePageView, EditProfileView


urlpatterns = [
    path('<int:pk>/',  ShowProfilePageView.as_view(), name='profile_link'),
    path('edit-profile/<int:pk>/',  EditProfileView.as_view(), name='edit_profile'),
    
]