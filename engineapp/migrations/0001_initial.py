# Generated by Django 5.1.2 on 2024-11-05 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название вакансии')),
                ('company', models.CharField(max_length=100, verbose_name='Название вакансии')),
                ('experience', models.CharField(default='Без опыта', max_length=80, verbose_name='Опыт работы')),
                ('salary', models.CharField(max_length=80, verbose_name='Оклад')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('skills', models.CharField(max_length=255, verbose_name='Навыки')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=14, verbose_name='Телефон')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineapp.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
