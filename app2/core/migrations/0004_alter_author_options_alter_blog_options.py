# Generated by Django 5.0.3 on 2024-04-01 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_blog_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Yazar', 'verbose_name_plural': 'Yazarlar'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Bloq', 'verbose_name_plural': 'Bloqlar'},
        ),
    ]
