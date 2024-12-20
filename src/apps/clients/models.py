from django.db import models
from django.utils.translation import gettext as _


class Client(models.Model):
    """
    Модель клиента/заказчика/постояльца
    :param int id: - Уникальный ID в рамках таблицы
    :param str first_name - Имя
    :param str last_name - Фамилия
    :param str middle_name - Отчество
    :param str status - string
    :param bool is_vip - bool
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

    # client_id = models.IntegerField(verbose_name="ID клиента", primary_key=True, unique=True)
    MALE = "male"
    FEMAIL = "femail"
    SEX_CHOICES = [
        (MALE, "муж"),
        (FEMAIL, "жен"),
    ]
    first_name = models.CharField(verbose_name=_("Имя"), max_length=64)
    middle_name = models.CharField(verbose_name=_("Отчество"), max_length=64)
    second_name = models.CharField(verbose_name=_("Фамилия"), max_length=64)
    is_vip = models.BooleanField(verbose_name=_("VIP-статус"), default=False)
    serial = models.PositiveIntegerField(verbose_name=_("Серия паспорта"))
    number = models.PositiveIntegerField(verbose_name=_("Номер паспорта"))
    police_department = models.CharField(verbose_name=_("Кем выдан"), max_length=250)
    police_department_id = models.PositiveIntegerField(
        verbose_name=_("Код подразделения")
    )
    date_issue = models.DateField(verbose_name=_("Дата выдачи"))
    sex = models.CharField(
        verbose_name=_("Пол"), max_length=10, choices=SEX_CHOICES, default=MALE
    )
    birth_date = models.DateField(verbose_name=_("Дата рождения"))
    birth_place = models.CharField(verbose_name=_("Место рождения"), max_length=300)
    registration = models.CharField(verbose_name=_("Адрес регистрации"), max_length=450)

    def get_sex(self):
        return "муж" if self.sex == "male" else "жен"

    def __str__(self):
        return f"{self.second_name} {self.first_name} {self.middle_name}"

    def full_name(self):
        return self.__str__()

    def passport_sn(self):
        return f"{self.serial} {self.number}"

    class Meta:
        verbose_name = _("Клиент")
        verbose_name_plural = _("Клиенты")
        db_table = "clients"
