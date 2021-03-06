# Generated by Django 3.2.4 on 2021-06-21 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(db_index=True, max_length=100, verbose_name='Количество')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('am', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipe.amount', verbose_name='Количество')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipe.product', verbose_name='Продукт')),
            ],
        ),
    ]
