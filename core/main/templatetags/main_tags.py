from django import template

register = template.Library()

from blog.models import  Category

#Вывод категорий сайта
@register.inclusion_tag('chunk/list_categories.html')
def show_categories():
    dataset=Category.objects.filter(is_draft=True)
    return {"dataset": dataset}


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