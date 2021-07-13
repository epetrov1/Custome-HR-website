# Generated by Django 3.2 on 2021-07-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumeuser', '0016_auto_20210709_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address_bg',
            field=models.CharField(max_length=300, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='company',
            name='address_de',
            field=models.CharField(max_length=300, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='company',
            name='address_en',
            field=models.CharField(max_length=300, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='company',
            name='company_name_bg',
            field=models.CharField(max_length=150, null=True, verbose_name='company_name'),
        ),
        migrations.AddField(
            model_name='company',
            name='company_name_de',
            field=models.CharField(max_length=150, null=True, verbose_name='company_name'),
        ),
        migrations.AddField(
            model_name='company',
            name='company_name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='company_name'),
        ),
        migrations.AddField(
            model_name='company',
            name='phone_bg',
            field=models.CharField(max_length=20, null=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='company',
            name='phone_de',
            field=models.CharField(max_length=20, null=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='company',
            name='phone_en',
            field=models.CharField(max_length=20, null=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='worker',
            name='first_name_bg',
            field=models.CharField(max_length=50, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='worker',
            name='first_name_de',
            field=models.CharField(max_length=50, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='worker',
            name='first_name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='worker',
            name='last_name_bg',
            field=models.CharField(max_length=50, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='worker',
            name='last_name_de',
            field=models.CharField(max_length=50, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='worker',
            name='last_name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='worker',
            name='phone_bg',
            field=models.CharField(max_length=20, null=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='worker',
            name='phone_de',
            field=models.CharField(max_length=20, null=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='worker',
            name='phone_en',
            field=models.CharField(max_length=20, null=True, verbose_name='phone'),
        ),
    ]