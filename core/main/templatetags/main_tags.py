from django import template

register = template.Library()

from blog.models import  Category
from profiles.models import  Profile

#Вывод категорий сайта
@register.inclusion_tag('chunk/list_categories.html')
def show_categories():
    dataset=Category.objects.filter(is_draft=True)
    return {"dataset": dataset}


#Вывод фото профиля в сайдбаре
@register.simple_tag()
def show_profile_logo(pk):
    dataset=Profile.objects.filter(pk=pk)
    for e in Profile.objects.filter(pk=pk):
        img= e.profile_pic
        if img == "":
            img="/profiles/6370834e9ed70200ed80232d0049a0d2.jpeg";
    return img


#формирование хлебных крошек
@register.simple_tag
def breadcrumb_schema():
    return "http://schema.org/BreadcrumbList"

@register.inclusion_tag('chunk/breadcrumb/breadcrumb_home.html')
def breadcrumb_home(url='/', title=''):
    return {
        'url': url,
        'title': title
    }
  
@register.inclusion_tag('chunk/breadcrumb/breadcrumb_item.html')
def breadcrumb_item(url, title, position):
    return {
        'url': url,
        'title': title,
        'position': position
    } 
 
@register.inclusion_tag('chunk/breadcrumb/breadcrumb_active.html')
def breadcrumb_active(url, title, position):
    return {
        'url': url,
        'title': title,
        'position': position
    }