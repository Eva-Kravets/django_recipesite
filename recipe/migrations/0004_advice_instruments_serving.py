# Generated by Django 3.2.4 on 2021-07-02 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_step'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Советы',
                'verbose_name_plural': 'Советы',
            },
        ),
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Инструменты',
                'verbose_name_plural': 'Инструменты',
            },
        ),
        migrations.CreateModel(
            name='Serving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Идеи подачи',
                'verbose_name_plural': 'Идеи подачи',
            },
        ),
    ]
