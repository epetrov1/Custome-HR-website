# Generated by Django 3.2 on 2021-07-31 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_alter_cv_driving_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='driving_category',
        ),
        migrations.AddField(
            model_name='cv',
            name='driving_category',
            field=models.CharField(blank=True, choices=[(1, 'B'), (2, 'B1'), (3, 'C'), (4, 'C1'), (5, 'D'), (6, 'D1'), (7, 'BE'), (8, 'C1E'), (9, 'CE'), (10, 'D1E'), (11, 'DE')], max_length=10, verbose_name='driving_category'),
        ),
    ]