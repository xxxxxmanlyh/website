# Generated by Django 2.1.5 on 2019-01-21 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190121_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='无名用户', max_length=128, unique=True),
        ),
    ]