# Generated by Django 5.0.3 on 2024-04-01 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_author_options_alter_blog_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
