# Generated by Django 3.2 on 2021-07-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0010_cv_expectet_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='position_1',
            field=models.CharField(choices=[('Position I aplly', 'Position I apply'), ('Different', 'Different')], default='Position I aplly', max_length=150),
        ),
        migrations.AddField(
            model_name='cv',
            name='position_2',
            field=models.CharField(choices=[('Position I aplly', 'Position I apply'), ('Different', 'Different')], default='Position I aplly', max_length=150),
        ),
        migrations.AddField(
            model_name='cv',
            name='position_3',
            field=models.CharField(choices=[('Position I aplly', 'Position I apply'), ('Different', 'Different')], default='Position I aplly', max_length=150),
        ),
    ]