# Generated by Django 5.0.4 on 2024-05-06 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=50)),
                ('date_time', models.DateTimeField()),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
