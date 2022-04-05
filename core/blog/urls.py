from django.urls import path
from . import views
from .views import BookListView, DetailPosts


urlpatterns = [
    path('<slug:slug>', views.DetailPosts, name='DetailPosts'), # new
    path('',  views.BookListView, name='BookListView'),

]