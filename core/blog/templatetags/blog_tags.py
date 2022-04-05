from django import template

register = template.Library()

from ..models import News, Category

@register.simple_tag()
def total_count_posts(id):
    count_posts = News.objects.filter(parent=id).count()
    return count_posts