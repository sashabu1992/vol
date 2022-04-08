from django.shortcuts import render
from .models import Category, News
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from django.views import generic
 


def BookListView(request):
    dataset=Category.objects.filter(is_draft=True)
    
    return render(
        request,
        'blog/blog.html',
        context={'dataset':dataset}
    )


def DetailPosts(request, slug_category):
    try:
        cat=Category.objects.get(slug=slug_category)
        id_cat = Category.objects.get(slug=slug_category).id
        detailcat=News.objects.filter(parent=id_cat)
    except Category.DoesNotExist:
        raise Http404("Категория не найдена")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'blog/detail-blog.html',
        context={'cat':cat,'detailcat':detailcat}
    )


def DetailNews(request, slug_category, slug_news):
    try:
        news=News.objects.get(slug=slug_news)
    except News.DoesNotExist:
        raise Http404("Статья не найдена")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'blog/detail-news.html',
        context={'news':news}
    )


