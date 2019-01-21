# Generated by Django 2.1.5 on 2019-01-12 13:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190112_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsortext', ckeditor.fields.RichTextField(verbose_name='赞助内容')),
            ],
            options={
                'verbose_name': '赞助内容',
                'verbose_name_plural': '赞助内容',
            },
        ),
    ]