from django.db import models
from .resources import units_of_measure

class Stock(models.Model):
    name = models.CharField(max_length=150, blank=False, verbose_name='Name:')
    oem = models.CharField(max_length=50, blank=True, verbose_name='OEM #:')
    id = models.AutoField(primary_key=True, verbose_name='Stock No.:', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Stock is Active?':)
    unit_of_measurement = units = models.CharField(max_length=255, choices=UNIT_CHOICES)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    threshold = models.PositiveIntegerField(verbose_name='Minimum stock (reorder) level:')
