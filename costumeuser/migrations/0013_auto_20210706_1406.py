# Generated by Django 3.2 on 2021-07-06 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costumeuser', '0012_auto_20210706_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_bg',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email_de',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email_en',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password_bg',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password_de',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password_en',
        ),
    ]