from django.db import models
from colorful.fields import RGBColorField

class Books(models.Model):
    name = models.CharField(max_length=256, blank=False, verbose_name="Назва")
    format = models.CharField(max_length=60, blank=False,
                              verbose_name="Формат")
    root = models.CharField(max_length=60, blank=False,
                            verbose_name="Корешок")
    bookmark = RGBColorField(blank=True, null=True, verbose_name="Закладка")
    captal = RGBColorField(blank=True, null=True, verbose_name="Каптал")
    photo = models.ImageField(blank=True, verbose_name="Фото", null=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        full_name = f'{self.name} | {self.format} | {self.root}'
        return full_name.strip()
