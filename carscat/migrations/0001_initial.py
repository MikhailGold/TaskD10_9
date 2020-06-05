# Generated by Django 3.0.6 on 2020-06-05 04:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=50, verbose_name='Производитель')),
                ('model', models.CharField(max_length=50, verbose_name='Модель авто')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2020)], verbose_name='Год выпуска')),
                ('transmission', models.SmallIntegerField(choices=[(1, 'Механика'), (2, 'Автомат'), (3, 'Робот'), (4, 'Вариатор')], default=1, verbose_name='Коробка передач')),
                ('color', models.SmallIntegerField(choices=[(1, 'Чёрный'), (2, 'Белый'), (3, 'Красный'), (4, 'Оранжевый'), (5, 'Жёлтый'), (6, 'Зелёный'), (7, 'Голубой'), (8, 'Синий'), (9, 'Фиолетовый'), (10, 'Металик')], default=1, verbose_name='Цвет')),
            ],
            options={
                'ordering': ('vendor', 'model'),
            },
        ),
    ]
