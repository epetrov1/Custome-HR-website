# Generated by Django 3.2 on 2021-07-31 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20210731_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='driving_category',
            field=models.ManyToManyField(blank=True, choices=[('B', 'B'), ('B1', 'B1'), ('C', 'C'), ('C1', 'C1'), ('D', 'D'), ('D1', 'D1'), ('BE', 'BE'), ('C1E', 'C1E'), ('CE', 'CE'), ('D1E', 'D1E'), ('DE', 'DE')], null=True, related_name='_category_cv_driving_category_+', to='category.Cv'),
        ),
    ]
