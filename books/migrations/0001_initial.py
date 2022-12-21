# Generated by Django 3.2 on 2023-04-23 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Назва')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('root', models.CharField(max_length=60, verbose_name='Корешок')),
                ('format', models.CharField(max_length=60, verbose_name='Формат')),
                ('bookmark', models.CharField(blank=True, default='', max_length=60, verbose_name='Закладка')),
                ('endpaper', models.CharField(blank=True, default='', max_length=60, verbose_name='Форзац')),
            ],
        ),
    ]
