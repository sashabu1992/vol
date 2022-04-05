from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Category, News



@admin.register(Category)
class Category(admin.ModelAdmin):
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
class News(admin.ModelAdmin):
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

