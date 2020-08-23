from django.db import models


class Order(models.Model):
    """
    Модель заказа
    :param int id: - Уникальный ID в рамках таблицы
    :param str status: - Статус заказа
    :param str type: - Тип заказа - Бронь/Отказ/Заселение/Выселение
    :param date date_start: - Дата открытия заказа
    :param date date_close: - Дата закрытия заказа
    :param int timestamp: - Timestamp
    :param int apartment_id: - Ссылка на конкретный номер
    :param int client_id: - Ссылка на конкретного клиента
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
    date_end = models.DateField(verbose_name="Дата закрытия заказа", null=True)
    timestamp = models.DateTimeField(verbose_name="Таймштамп", auto_now_add=True)
    id_client = models.ForeignKey(to='clients.Client', on_delete=models.DO_NOTHING, null=True)
    id_apartment = models.ForeignKey(to='apartments.Apartment', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'Заказ от: {self.date_start} - {self.get_status()} - {self.get_type()}'

    def get_status(self):
        """Функция возвращает статус заказа"""
        return 'Открыт' if self.status == 'open' else 'Закрыт'

    def get_type(self):
        """Функция позвращает тип заказа"""
        if self.type == 'booked':
            t = 'Забронировано'
        elif self.type == 'revoked':
            t = 'Отказ'
        elif self.type == 'checkin':
            t = 'Заселение'
        elif self.type == 'eviction':
            t = 'Выселение'
        else:
            t = None
        return t

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        db_table = "orders"
