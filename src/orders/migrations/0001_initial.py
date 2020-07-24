# Generated by Django 3.0.8 on 2020-07-22 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartments', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('open', 'Открыт'), ('close', 'Закрыт')], default='open', max_length=30, verbose_name='Статус заказа')),
                ('type', models.CharField(choices=[('booked', 'Забронировано'), ('revoked', 'Отказ'), ('checkin', 'Заселение'), ('eviction', 'Выселение')], default='booked', max_length=30, verbose_name='Тип заказа')),
                ('date_start', models.DateField(verbose_name='Дата открытия заказа')),
                ('date_end', models.DateField(null=True, verbose_name='Дата закрытия заказа')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Таймштамп')),
                ('id_apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apartments.Apartment')),
                ('id_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clients.Client')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'orders',
            },
        ),
    ]
