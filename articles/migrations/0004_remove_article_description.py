# Generated by Django 2.1.7 on 2019-03-06 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='description',
        ),
    ]
