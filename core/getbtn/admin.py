from django.contrib import admin
from import_export import resources
# Register your models here.
# Register your models here.
from .models import GetBtn


@admin.register(GetBtn)
class GetBtn(admin.ModelAdmin):
    list_display = ('vk', 'telegram', 'instagram')
   

