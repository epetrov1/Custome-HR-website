# Generated by Django 3.2 on 2021-07-06 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costumeuser', '0013_auto_20210706_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='first_name_bg',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='first_name_de',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='first_name_en',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='last_name_bg',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='last_name_de',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='last_name_en',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='phone_bg',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='phone_de',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='phone_en',
        ),
    ]
