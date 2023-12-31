# Generated by Django 5.0 on 2023-12-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='ImagesForHomepage')),
                ('htmlid', models.CharField(max_length=50)),
                ('href', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('link', models.URLField()),
            ],
        ),
    ]
