# Generated by Django 2.0.2 on 2018-02-15 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
