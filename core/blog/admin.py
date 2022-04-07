from django.contrib import admin
from import_export import resources
# Register your models here.
# Register your models here.
from .models import Category, News
from import_export.admin import ImportExportModelAdmin



@admin.register(Category)
class Category(ImportExportModelAdmin):
    list_display = ('h1', 'created', 'is_draft', 'slug')
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


@admin.register(News)
class News(ImportExportModelAdmin):
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

