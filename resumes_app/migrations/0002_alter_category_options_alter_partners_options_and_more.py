# Generated by Django 4.0.3 on 2022-03-19 13:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resumes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'Партнеры', 'verbose_name_plural': 'Партнеры'},
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={'verbose_name': 'Резюме', 'verbose_name_plural': 'Резюме'},
        ),
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name': 'Закладки', 'verbose_name_plural': 'Закладки'},
        ),
        migrations.AlterUniqueTogether(
            name='wishlist',
            unique_together={('user', 'wished_resume')},
        ),
    ]
