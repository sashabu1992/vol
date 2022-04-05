from django.urls import path
from . import views
from .views import BookListView, DetailPosts, DetailNews


urlpatterns = [
    path('<slug:slug_category>/<slug:slug_news>', views.DetailNews, name='DetailNews'), # new
    path('<slug:slug_category>/', views.DetailPosts, name='DetailPosts'), # new
    path('',  views.BookListView, name='BookListView'),
]