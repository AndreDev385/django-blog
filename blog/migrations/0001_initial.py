# Generated by Django 3.2.7 on 2021-09-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name="Author's Name")),
                ('last_name', models.CharField(max_length=255, verbose_name="Author's Last Name")),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('state', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('state', models.BooleanField(default=True, verbose_name='Activate/Deactivate')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]