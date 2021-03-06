# Generated by Django 4.0.3 on 2022-04-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetBtn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk', models.CharField(blank=True, max_length=350, null=True, verbose_name='Вконтакте')),
                ('telegram', models.CharField(blank=True, max_length=350, null=True, verbose_name='Telegram')),
                ('instagram', models.CharField(blank=True, max_length=350, null=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Скрипт',
                'verbose_name_plural': 'Скрипты',
                'ordering': ('vk',),
            },
        ),
    ]
