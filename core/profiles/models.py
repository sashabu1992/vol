from django.conf import settings
from django.db import models
import uuid
import os
from PIL import Image


def get_file_path_profiles(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('profiles/', filename)

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
     verbose_name="Пользователь")
    bio=models.TextField(null=True, blank=True, verbose_name="Краткое описание")
    city=models.CharField(max_length=150, null=True, blank=True, verbose_name="Город")
    user_phone = models.CharField(max_length=140, blank=True, null=True, verbose_name="Телефон")
    profile_pic = models.ImageField(null=True, blank=True, upload_to=get_file_path_profiles, verbose_name="Фотография")
    vk = models.CharField(max_length=350, null=True, blank=True, verbose_name="Вконтакте")
    telegram = models.CharField(max_length=350, null=True, blank=True, verbose_name="Telegram")
    instagram = models.CharField(max_length=350, null=True, blank=True, verbose_name="Instagram")
    
    def save(self, *args, **kwargs):
        # Сначала - обычное сохранение
        super(Profile, self).save(*args, **kwargs)

        # Проверяем, указан фото
        if self.profile_pic:
            filepath = self.profile_pic.path

            image = Image.open(filepath)
                # resize - безопасная функция, она создаёт новый объект, а не
                # вносит изменения в исходный, поэтому так
            image = image.resize(
                    (200,  # Сохраняем пропорции
                    200),
                    Image.ANTIALIAS
                )
                # И не забыть сохраниться
            image.save(filepath)
    class Meta:
        ordering = ('user',)
        verbose_name = ('Профиль')
        verbose_name_plural = ('Профили')

    def __str__(self):
        return str(self.user)