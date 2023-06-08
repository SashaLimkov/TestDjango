# Generated by Django 4.2.1 on 2023-05-23 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('segregator', '0004_alter_entity_body_alter_entity_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='document',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='entity',
        ),
        migrations.AlterField(
            model_name='entity',
            name='slug',
            field=models.SlugField(verbose_name='Игнорировать это поле'),
        ),
        migrations.AddField(
            model_name='doc',
            name='entity',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='segregator.entity', verbose_name='Оглавления'),
        ),
    ]
