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


def DetailPosts(request, slug):
    try:
        book_id=Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        raise Http404("Статья не найдена")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'blog/news.html',
        context={'book':book_id,}
    )
