from django.db import models


class Apartment(models.Model):
    """
    Модель номера/апартамента
    :param int id: - Уникальный ID в рамках таблицы
    :param int name - Имя номера (порядковый номер номера =) )
    :param str status - Статус номер - Свободен/Занят/Забронирован/На обслуживании
    :param float day_price - Стоимость за сутки
    :param float night_price - Стоимость за ночь
    :param str apartment_type - Люкс/Полу-люкс/Стандарт/Эконом/Для молодожен;
    :param int floor - Этаж
    :param str description - Описание номера
    """
    AP_STATUS_FREE = 'free'
    AP_STATUS_BUSY = 'busy'
    AP_STATUS_BOOKING = 'booking'
    AP_STATUS_MAINTENANCE = 'maintenance'
    APARTMENT_STATUS_CHOICES = [
        (AP_STATUS_FREE, 'Свободен'),
        (AP_STATUS_BUSY, 'Занят'),
        (AP_STATUS_BOOKING, 'Забронирован'),
        (AP_STATUS_MAINTENANCE, 'На обслуживании'),
    ]
    AP_TYPE_LUXURY = 'luxary'
    AP_TYPE_HALFLUXURY = 'halfluxury'
    AP_TYPE_STANDART = 'standart'
    AP_TYPE_ECONOMY = 'economy'
    AP_TYPE_MARRIED = 'married'
    APARTMENT_TYPE_CHOICES = [
        (AP_TYPE_LUXURY, 'Люкс'),
        (AP_TYPE_HALFLUXURY, 'Полу-люкс'),
        (AP_TYPE_STANDART, 'Стандарт'),
        (AP_TYPE_ECONOMY, 'Эконом'),
        (AP_TYPE_MARRIED, 'Для молодожен'),
    ]

    name = models.PositiveSmallIntegerField(verbose_name="Номер апартамента", unique=True)
    status = models.CharField(verbose_name="Статус",
                              max_length=25,
                              choices=APARTMENT_STATUS_CHOICES,
                              default=AP_STATUS_FREE)
    day_price = models.IntegerField(verbose_name="Стоимость за сутки")
    night_price = models.IntegerField(verbose_name="Стоимость за ночь")
    apartment_type = models.CharField(verbose_name="Тип",
                                      max_length=25,
                                      choices=APARTMENT_TYPE_CHOICES,
                                      default=AP_TYPE_STANDART)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f'Номер: {self.name} :  Тип номера: {self.get_apartment_type()} - Статуст: {self.get_apartment_status()}'

    def get_apartment_type(self):
        if self.apartment_type == 'luxary':
            apt = 'Люкс'
        elif self.apartment_type == 'halfluxury':
            apt = 'Полу-люкс'
        elif self.apartment_type == 'standart':
            apt = 'Стандарт'
        elif self.apartment_type == 'economy':
            apt = 'Эконом'
        else:
            apt = 'Для молодожен'
        return apt

    def get_apartment_status(self):
        if self.status == 'free':
            aps = 'Свободен'
        elif self.status == 'busy':
            aps = 'Занят'
        elif self.status == 'booking':
            aps = 'Забронирован'
        else:
            aps = 'На обслуживании'
        return aps

    class Meta:
        verbose_name = "Апартамент"
        verbose_name_plural = "Апартаменты"
        db_table = "apartments"
