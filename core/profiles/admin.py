from django.contrib import admin
from import_export import resources
# Register your models here.
# Register your models here.
from .models import Profile


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user', 'bio', 'birthday')





