# Generated by Django 2.2.1 on 2019-07-22 09:55

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='文章内容'),
        ),
    ]