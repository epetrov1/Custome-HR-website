# Generated by Django 3.2 on 2021-07-26 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_cv_cv_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='position_1',
            field=models.CharField(choices=[('Position I aplly', 'Position I apply'), ('Different', 'Different')], max_length=150, verbose_name='position_1'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='position_2',
            field=models.CharField(choices=[('Position I aplly', 'Position I apply'), ('Different', 'Different')], max_length=150, verbose_name='position_2'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='position_3',
            field=models.CharField(choices=[('Position I aplly', 'Position I apply'), ('Different', 'Different')], max_length=150, verbose_name='position_3'),
        ),
    ]
