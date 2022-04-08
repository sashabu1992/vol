from django.urls import path, re_path
from . import views
from .views import BookListView, DetailPosts, DetailNews


urlpatterns = [
    path('',  views.BookListView, name='BookListView'),
    path('<slug:slug_category>/', views.DetailPosts, name='DetailPosts'), # new
    path('<slug:slug_category>/<slug:slug_news>/', views.DetailNews, name='DetailNews'), # new

    
]