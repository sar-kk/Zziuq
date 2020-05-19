# Generated by Django 3.0.6 on 2020-05-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('mężczyzna', '♂'), ('kobieta', '♀')], default='♀', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'użytkownik',
                'verbose_name_plural': 'użytkownik',
                'ordering': ['-c_time'],
            },
        ),
    ]
