# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class ApisDistricts(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    adm2_en = models.TextField(db_column='ADM2_EN', blank=True, null=True)  # Field name made lowercase.
    adm2_pcode = models.TextField(db_column='ADM2_PCODE', blank=True, null=True)  # Field name made lowercase.
    adm2_bn = models.TextField(db_column='ADM2_BN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apis_districts'


class ApisDivisions(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    adm1_en = models.TextField(db_column='ADM1_EN', blank=True, null=True)  # Field name made lowercase.
    adm1_pcode = models.BigIntegerField(db_column='ADM1_PCODE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apis_divisions'


class ApisParameter(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apis_parameter'


class ApisSource(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apis_source'


class ApisUpazila(models.Model):
    # upazila_id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    division = models.TextField(blank=True, null=True)
    adm1_pcode = models.BigIntegerField(db_column='ADM1_PCODE', blank=True, null=True)  # Field name made lowercase.
    adm2_pcode = models.BigIntegerField(db_column='ADM2_PCODE', blank=True, null=True)  # Field name made lowercase.
    adm3_pcode = models.BigIntegerField(db_column='ADM3_PCODE', blank=True, null=True)  # Field name made lowercase.
    shape_leng_up = models.TextField(blank=True, null=True)
    shape_area_up = models.TextField(blank=True, null=True)
    shape_leng_ds = models.TextField(blank=True, null=True)
    shape_area_ds = models.TextField(blank=True, null=True)
    shape_leng_dv = models.TextField(blank=True, null=True)
    shape_area_dv = models.TextField(blank=True, null=True)
    name_bn = models.TextField(blank=True, null=True)
    district_bn = models.TextField(blank=True, null=True)
    division_bn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apis_upazila'


class ApisUpazilaForecastDaily(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    forecast_date = models.DateField(blank=True, null=True)
    step_start = models.DateTimeField(blank=True, null=True)
    step_end = models.DateTimeField(blank=True, null=True)
    val_min = models.FloatField(blank=True, null=True)
    val_avg = models.FloatField(blank=True, null=True)
    val_max = models.FloatField(blank=True, null=True)
    val_avg_day = models.FloatField(blank=True, null=True)
    val_avg_night = models.FloatField(blank=True, null=True)
    parameter_id = models.BigIntegerField(blank=True, null=True)
    source_id = models.BigIntegerField(blank=True, null=True)
    upazila_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apis_upazila_forecast_daily'


class ApisUpazilaForecastSteps(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    forecast_date = models.DateField(blank=True, null=True)
    step_start = models.DateTimeField(blank=True, null=True)
    step_end = models.DateTimeField(blank=True, null=True)
    val_min = models.FloatField(blank=True, null=True)
    val_avg = models.FloatField(blank=True, null=True)
    val_max = models.FloatField(blank=True, null=True)
    parameter_id = models.BigIntegerField(blank=True, null=True)
    source_id = models.BigIntegerField(blank=True, null=True)
    upazila_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apis_upazila_forecast_steps'

class DjangoMigrations(models.Model):
    # id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


