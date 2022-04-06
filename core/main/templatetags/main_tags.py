from django import template

register = template.Library()

from blog.models import  Category


@register.inclusion_tag('chunk/list_categories.html')
def show_categories():
    dataset=Category.objects.filter(is_draft=True)
    return {"dataset": dataset}