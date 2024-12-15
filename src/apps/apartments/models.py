from django.db import models
from django.utils.translation import gettext as _


class Apartment(models.Model):
    """
    Room/apartment model
    :param int id: - Unique ID within the table
    :param int name - Room name (room sequence number =) )
    :param str status - Room status - Free/Used/Reserved/Maintained
    :param float day_price - Price per day
    :param float night_price - Rate per night
    :param str apartment_type - Suite/Semi-suite/Standard/Economy/Honeymoon;
    :param int floor - Floor
    :param str description - Room description
    """

    AP_STATUS_FREE = "free"
    AP_STATUS_BUSY = "busy"
    AP_STATUS_BOOKING = "booking"
    AP_STATUS_MAINTENANCE = "maintenance"
    APARTMENT_STATUS_CHOICES = [
        (AP_STATUS_FREE, _("Free")),
        (AP_STATUS_BUSY, _("Busy")),
        (AP_STATUS_BOOKING, _("Booking")),
        (AP_STATUS_MAINTENANCE, _("Maintenance")),
    ]
    AP_TYPE_LUXURY = "luxary"
    AP_TYPE_HALFLUXURY = "halfluxury"
    AP_TYPE_STANDART = "standart"
    AP_TYPE_ECONOMY = "economy"
    AP_TYPE_MARRIED = "married"
    APARTMENT_TYPE_CHOICES = [
        (AP_TYPE_LUXURY, _("Luxary")),
        (AP_TYPE_HALFLUXURY, _("Half luxury")),
        (AP_TYPE_STANDART, _("Standart")),
        (AP_TYPE_ECONOMY, _("Economy")),
        (AP_TYPE_MARRIED, _("Married")),
    ]

    name = models.PositiveSmallIntegerField(
        verbose_name=_("Apartment number"), unique=True
    )
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=25,
        choices=APARTMENT_STATUS_CHOICES,
        default=AP_STATUS_FREE,
    )
    day_price = models.IntegerField(verbose_name=_("Cost per day"))
    night_price = models.IntegerField(verbose_name=_("Cost per night"))
    apartment_type = models.CharField(
        verbose_name=_("Apartment type"),
        max_length=25,
        choices=APARTMENT_TYPE_CHOICES,
        default=AP_TYPE_STANDART,
    )
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return _(f"Number: {self.name} :  Apartment type: {self.get_apartment_type()} - Status: {self.get_apartment_status()}")

    def get_apartment_type(self):
        if self.apartment_type == "luxary":
            apt = _("Luxary")
        elif self.apartment_type == "halfluxury":
            apt = _("Half luxury")
        elif self.apartment_type == "standart":
            apt = _("Standart")
        elif self.apartment_type == "economy":
            apt = _("Economy")
        else:
            apt = _("Married")
        return apt

    def get_apartment_status(self):
        if self.status == "free":
            aps = _("Free")
        elif self.status == "busy":
            aps = _("Busy")
        elif self.status == "booking":
            aps = _("Booking")
        else:
            aps = _("Maintenance")
        return aps

    class Meta:
        verbose_name = _("Apartment")
        verbose_name_plural = _("Apartments")
        db_table = "apartments"
