# Generated by Django 3.2 on 2021-06-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumeuser', '0006_alter_worker_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(default='media/default.jpeg', upload_to='profile_pics'),
        ),
    ]
