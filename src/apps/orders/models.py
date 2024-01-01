from django.db import models


class Order(models.Model):
    """
    Модель заказа
    :param int id: - Уникальный ID в рамках таблицы
    :param str status: - Статус заказа
    :param date date_start: - Дата открытия заказа
    :param date date_close: - Дата закрытия заказа
    :param int timestamp: - Timestamp
    :param int id_apartment: - Ссылка на конкретный номер
    :param int id_client: - Ссылка на конкретного клиента
    """
    OPEN = 'open'
    CLOSE = 'close'
    STATUS_CHOICES = [
        (OPEN, 'Открыт'),
        (CLOSE, 'Закрыт')
    ]
    status = models.CharField(verbose_name="Статус заказа",
                              max_length=30,
                              choices=STATUS_CHOICES,
                              default=OPEN)
    date_start = models.DateField(verbose_name="Дата открытия заказа")
    date_end = models.DateField(verbose_name="Дата закрытия заказа", null=True)
    timestamp = models.DateTimeField(verbose_name="Таймштамп", auto_now_add=True)
    id_client = models.ForeignKey(to='clients.Client', on_delete=models.DO_NOTHING, null=True)
    id_apartment = models.ForeignKey(to='apartments.Apartment', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'Заказ № {self.id} от: {self.date_start} - {self.get_status()}'

    def get_status(self):
        """Функция возвращает статус заказа"""
        return 'Открыт' if self.status == 'open' else 'Закрыт'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        db_table = "orders"
