# Generated by Django 3.2 on 2023-04-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20230425_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='endpaper',
        ),
        migrations.AddField(
            model_name='books',
            name='captal',
            field=models.CharField(blank=True, default='#FFFFFF', max_length=20, verbose_name='Каптал'),
        ),
    ]