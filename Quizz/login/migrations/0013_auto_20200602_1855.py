# Generated by Django 3.0.6 on 2020-06-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20200602_1739'),
        ('login', '0012_auto_20200602_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='geography',
            field=models.ManyToManyField(blank=True, related_name='formats', to='category.Geography'),
        ),
    ]
