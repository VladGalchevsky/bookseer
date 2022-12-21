from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=256, blank=False, verbose_name="Назва")
    photo = models.ImageField(blank=True, verbose_name="Фото", null=True)
    root = models.CharField(max_length=60, blank=False,
                            verbose_name="Корешок")
    format = models.CharField(max_length=60, blank=False,
                              verbose_name="Формат")
    bookmark = models.CharField(max_length=60, blank=True, default='',
                                verbose_name="Закладка")
    endpaper = models.CharField(max_length=60, blank=True, default='',
                                verbose_name="Форзац")
