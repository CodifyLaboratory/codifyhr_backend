# Generated by Django 3.2.12 on 2022-03-18 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='image',
        ),
    ]
