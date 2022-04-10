from django.db import models

# Create your models here.

class GetBtn(models.Model):

    vk = models.CharField(max_length=350, null=True, blank=True, verbose_name="Вконтакте")
    telegram = models.CharField(max_length=350, null=True, blank=True, verbose_name="Telegram")
    instagram = models.CharField(max_length=350, null=True, blank=True, verbose_name="Instagram")
    
 
    class Meta:
        ordering = ('vk',)
        verbose_name = ('Скрипт')
        verbose_name_plural = ('Скрипты')

    def __str__(self):
        return str(self.vk)