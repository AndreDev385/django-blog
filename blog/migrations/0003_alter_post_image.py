# Generated by Django 3.2.7 on 2021-09-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(max_length=257, verbose_name='Image'),
        ),
    ]
