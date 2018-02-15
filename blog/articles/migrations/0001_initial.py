# Generated by Django 2.0.2 on 2018-02-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
