# Generated by Django 4.2.1 on 2023-05-23 09:07

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file', verbose_name='Файл')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True, verbose_name='Название')),
                ('body', models.TextField(verbose_name='Содержание')),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('document', models.ManyToManyField(related_name='documents', to='segregator.doc', verbose_name='файлы')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='segregator.entity', verbose_name='Родительская сущность')),
            ],
            options={
                'verbose_name': 'Сущность',
                'verbose_name_plural': 'Сущности',
                'unique_together': {('parent', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='doc',
            name='entity',
            field=models.ManyToManyField(related_name='entities', to='segregator.entity', verbose_name='Оглавления'),
        ),
    ]
