# Generated by Django 3.0.8 on 2020-07-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveSmallIntegerField(verbose_name='Номер апартамента')),
                ('status', models.CharField(choices=[('free', 'Свободен'), ('busy', 'Занят'), ('booking', 'Забронирован'), ('maintenance', 'На обслуживании')], default='free', max_length=25, verbose_name='Статус')),
                ('day_price', models.IntegerField(verbose_name='Стоимость за сутки')),
                ('night_price', models.IntegerField(verbose_name='Стоимость за ночь')),
                ('apartment_type', models.CharField(choices=[('luxary', 'Люкс'), ('halfluxury', 'Полу-люкс'), ('standart', 'Стандарт'), ('economy', 'Эконом'), ('married', 'Для молодожен')], default='standart', max_length=25, verbose_name='Тип')),
                ('floor', models.PositiveSmallIntegerField(verbose_name='Этаж')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Апартамент',
                'verbose_name_plural': 'Апартаменты',
                'db_table': 'apartments',
            },
        ),
    ]
