from django.db import models


class Apartment(models.Model):
    """
    Модель номера/апартамента
    id - integer
    name - integer
    status - string
    day_price - float
    night_price - float
    apartment_type - Люкс/Полулюкс/Стандарт/Эконом/Для молодожен;
    floor - int
    description - charfield
    id_clients - FK
    id_orders - FK
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

    name = models.PositiveSmallIntegerField(verbose_name="Номер апартамента")
    status = models.CharField(verbose_name="Статус",
                              max_length=25,
                              choices=APARTMENT_STATUS_CHOICES,
                              default=AP_STATUS_FREE)
    day_price = models.DecimalField(verbose_name="Стоимость за сутки", decimal_places=4, max_digits=8)
    night_price = models.DecimalField(verbose_name="Стоимость за ночь", decimal_places=4, max_digits=8)
    apartment_type = models.CharField(verbose_name="Тип",
                                      max_length=25,
                                      choices=APARTMENT_TYPE_CHOICES,
                                      default=AP_TYPE_STANDART)
    floor = models.PositiveSmallIntegerField(verbose_name="Этаж")
    description = models.CharField(verbose_name="Описание", max_length=500)
    id_clients = models.ForeignKey('Client', on_delete=models.DO_NOTHING)
    id_orders = models.ForeignKey('Order', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} - {self.apartment_type}'

    class Meta:
        verbose_name = "Апартамент"
        verbose_name_plural = "Апартаменты"


class Client(models.Model):
    """
    Модель клиента/заказчика/постояльца
    id - integer
    first_name - string
    last_name - string
    middle_name - string
    status - string
    is_vip - bool
    passport_id – FK
    """
    first_name = models.CharField(verbose_name="Имя", max_length=64)
    middle_name = models.CharField(verbose_name="Отчество", max_length=64)
    second_name = models.CharField(verbose_name="Фамилия", max_length=64)
    status = models.CharField(verbose_name="Статус", max_length=64)
    is_vip = models.BooleanField(verbose_name="VIP-статус", default=False)
    id_passports = models.OneToOneField('Passport', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.second_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Passport(models.Model):
    """
    Модель паспорта клиента

    id
    serial
    number
    police_department
    police_department_id
    date_issue
    sex
    birth_date
    birth_place
    registration
    image - not presented
    """
    MALE = 'male'
    FEMAIL = 'femail'
    SEX_CHOICES = [
        (MALE, 'муж'),
        (FEMAIL, 'жен'),
    ]
    serial = models.PositiveIntegerField(verbose_name='Серия паспорта')
    number = models.PositiveIntegerField(verbose_name='Номер паспорта')
    police_department = models.CharField(verbose_name='Кем выдан', max_length=250)
    police_department_id = models.PositiveSmallIntegerField(verbose_name='Код подразделения')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    sex = models.CharField(verbose_name="Пол",
                           max_length=10,
                           choices=SEX_CHOICES,
                           default=MALE)

    def __str__(self):
        return f'{self.serial} {self.number}'

    class Meta:
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорта"


class Order(models.Model):
    """
    Модель заказов
    id
    status
    type - Бронь / Отказ / Заселение / Выселение
    date_start
    date_close
    timestamp
    apartment_id - FK
    client_id - FK
    """
    BOOKED = 'booked'
    REVOKED = 'revoked'
    CHECKIN = 'checkin'
    EVICTION = 'eviction'
    OPEN = 'open'
    CLOSE = 'close'
    TYPE_CHOICES = [
        (BOOKED, 'Забронировано'),
        (REVOKED, 'Отказ'),
        (CHECKIN, 'Заселение'),
        (EVICTION, 'Выселение'),
    ]
    STATUS_CHOICES = [
        (OPEN, 'Открыт'),
        (CLOSE, 'Закрыт')
    ]
    status = models.CharField(verbose_name="Статус заказа",
                              max_length=30,
                              choices=STATUS_CHOICES,
                              default=OPEN)
    type = models.CharField(verbose_name="Тип заказа",
                            max_length=30,
                            choices=TYPE_CHOICES,
                            default=BOOKED)
    date_start = models.DateField(verbose_name="Дата открытия заказа")
    date_end = models.DateField(verbose_name="Дата закрытия заказа")
    timestamp = models.DateTimeField(verbose_name="Таймштамп", auto_now_add=True)

    def __str__(self):
        return f'{self.status} - {self.type}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
