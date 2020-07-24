from django.db import models


class Client(models.Model):
    """
    Модель клиента/заказчика/постояльца
    :param int id: - Уникальный ID в рамках таблицы
    :param str first_name - Имя
    :param str last_name - Фамилия
    :param str middle_name - Отчество
    :param str status - string
    :param bool is_vip - bool
    :param int passport_id – FK
    """
    # client_id = models.IntegerField(verbose_name="ID клиента", primary_key=True, unique=True)
    first_name = models.CharField(verbose_name="Имя", max_length=64)
    middle_name = models.CharField(verbose_name="Отчество", max_length=64)
    second_name = models.CharField(verbose_name="Фамилия", max_length=64)
    status = models.CharField(verbose_name="Статус", max_length=64)
    is_vip = models.BooleanField(verbose_name="VIP-статус", default=False)
    id_passport = models.OneToOneField('Passport', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.second_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        db_table = "clients"


class Passport(models.Model):
    """
    Модель паспорта клиента

    :param int id: - Уникальный ID в рамках таблицы
    :param int serial: - Серия паспорта
    :param int number: - Номер паспорта
    :param str police_department: - Кем выдано
    :param int police_department_id: - Код подразделения
    :param date date_issue: - Дата выдачи
    :param str sex: - Пол
    :param date birth_date: - Дата рождения
    :param date birth_place: - Место рождения
    :param str registration: - Адрес регистрации
    :param byte image: - Скан паспорта TODO: Доделать возможность прикреплять скан парспорта
    """
    MALE = 'male'
    FEMAIL = 'femail'
    SEX_CHOICES = [
        (MALE, 'муж'),
        (FEMAIL, 'жен'),
    ]
    # passport_id = models.IntegerField(verbose_name="ID пасспорта", primary_key=True, unique=True)
    serial = models.PositiveIntegerField(verbose_name='Серия паспорта')
    number = models.PositiveIntegerField(verbose_name='Номер паспорта')
    police_department = models.CharField(verbose_name='Кем выдан', max_length=250)
    police_department_id = models.PositiveIntegerField(verbose_name='Код подразделения')
    date_issue = models.DateField(verbose_name='Дата выдачи')
    sex = models.CharField(verbose_name="Пол",
                           max_length=10,
                           choices=SEX_CHOICES,
                           default=MALE)
    birth_date = models.DateField(verbose_name='Дата рождения')
    birth_place = models.CharField(verbose_name='Место рождения', max_length=300)
    registration = models.CharField(verbose_name='Адрес регистрации', max_length=450)

    def __str__(self):
        return f'Серия: {self.serial} Номер: {self.number}\nПол: {self.get_sex()}'

    def get_sex(self):
        return 'муж' if self.sex == 'male' else 'жен'

    class Meta:
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорта"
        db_table = "passports"

