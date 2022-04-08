from django.contrib import admin
from import_export import resources
# Register your models here.
# Register your models here.
from .models import Category, News
from import_export.admin import ImportExportModelAdmin
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.html import format_html

@admin.register(Category)
class Category(ImportExportModelAdmin):
    search_fields = ("h1", )
    list_display = ('h1', 'created', 'is_draft', 'slug', 'view_students_link')
    fieldsets = (
        ('Содержимое', {
            'fields': ('h1','image_zast', 'introtext', 'post')
        }),
        ('SEO', {
            'fields': ('title','description', 'slug')
        }),        
        ('Настройки', {
            'fields': ('created', 'modified', 'is_draft')
        }),
    )
    readonly_fields = ('created', 'modified')
    list_filter = ('is_draft',)


    def view_students_link(self, obj):
        count = obj.parent.count()
        url = (
             reverse("admin:blog_news_changelist")
            + "?"
            + urlencode({"parent__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">Всего: {} </a>', url, count)
    view_students_link.short_description = "Статей"


@admin.register(News)
class News(ImportExportModelAdmin):
    search_fields = ("h1", )
    list_display = ('h1', 'created', 'is_draft', 'slug')
    fieldsets = (
        ('Содержимое', {
            'fields': ('parent', 'h1','image_zast', 'introtext', 'post')
        }),
        ('SEO', {
            'fields': ('title','description', 'slug')
        }),        
        ('Настройки', {
            'fields': ('created', 'modified', 'is_draft')
        }),
    )
    readonly_fields = ('created', 'modified')
    list_filter = ('parent', 'is_draft')

