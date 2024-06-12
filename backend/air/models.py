from django.db import models

MAX_DIGITS = 30
DECIMAL_PLACES = 20


# Create your models here.
class AirData(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    province_id = models.IntegerField()
    aqi = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    pm25 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    pm10 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    so2 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    no2 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    co = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    o3 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    u = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    v = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    temp = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    rh = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    psfc = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)


class YearData(models.Model):
    province_id = models.IntegerField()
    year = models.IntegerField()
    average_aqi = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    average_pm25 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    average_pm10 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    average_so2 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    average_no2 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    average_co = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    average_o3 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
