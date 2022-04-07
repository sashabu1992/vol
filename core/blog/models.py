from django.db import models
from slugify import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    """СЕО натсрйоки"""
    title = models.CharField(max_length=255, verbose_name="Заголовок Title")
    description = models.CharField(max_length=350, verbose_name="Заголовок Description", blank=True)
    
    """Основные данные категории"""
    h1 = models.CharField(max_length=255, verbose_name="Заголовок H1")
    image_zast = models.ImageField(upload_to='cat/image', verbose_name="Заставка категории", blank=True)
    post = RichTextField( verbose_name="Содержание", blank=True)
    introtext = models.TextField(max_length=1000, verbose_name="Краткое описание", blank=True)

    created = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата создания")
    modified = models.DateField(auto_now=True, verbose_name="Дата изменения")
    is_draft = models.BooleanField(default=True, verbose_name="Опубликован")
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name="URl")


    class Meta:
        ordering = ('title',)
        verbose_name = ('Категорию')
        verbose_name_plural = ('Категории')


    def __str__(self):
        """Return title and username."""
        return str(self.h1) 


    def get_absolute_url(self):
        return reverse('DetailPosts', kwargs={'slug_category': self.slug}) # new

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)


class News(models.Model):
    """СЕО натсрйоки"""
    title = models.CharField(max_length=255, verbose_name="Заголовок Title")
    description = models.CharField(max_length=350, verbose_name="Заголовок Description", blank=True)
    
    """Основные данные категории"""
    parent = models.OneToOneField(Category, on_delete=models.PROTECT, verbose_name="Категория", related_name="parent")
    h1 = models.CharField(max_length=255, verbose_name="Заголовок H1")
    image_zast = models.ImageField(upload_to='cat/image', verbose_name="Заставка статьи", blank=True)
    post = RichTextField( verbose_name="Содержание", blank=True)
    introtext = models.TextField(max_length=1000, verbose_name="Краткое описание", blank=True)

    created = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата создания")
    modified = models.DateField(auto_now=True, verbose_name="Дата изменения")
    is_draft = models.BooleanField(default=True, verbose_name="Опубликован")
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name="URl")


    class Meta:
        ordering = ('title',)
        verbose_name = ('Статью')
        verbose_name_plural = ('Статьи')


    def __str__(self):
        """Return title and username."""
        return str(self.h1) 
    
    def get_absolute_url(self):
        return reverse('DetailNews', kwargs={'slug_news': self.slug}) # new

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super(News, self).save(*args, **kwargs)