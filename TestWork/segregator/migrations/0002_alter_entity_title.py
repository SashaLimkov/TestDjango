# Generated by Django 4.1.7 on 2023-02-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segregator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
    ]
