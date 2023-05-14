# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.contrib.gis.db import models
# from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ObserveData(models.Model):
    stcode = models.CharField(db_column='stCode', max_length=12)  # Field name made lowercase.
    date_time = models.CharField(max_length=20)
    pointname = models.CharField(max_length=40)
    max_norm = models.CharField(max_length=14)
    min_norm = models.CharField(max_length=14)
    sunrise = models.CharField(db_column='SunRise', max_length=20)  # Field name made lowercase.
    sunset = models.CharField(db_column='SunSet', max_length=20)  # Field name made lowercase.
    morning = models.CharField(db_column='Morning', max_length=20)  # Field name made lowercase.
    evenning = models.CharField(db_column='Evenning', max_length=20)  # Field name made lowercase.
    moonrise = models.CharField(db_column='MoonRise', max_length=20)  # Field name made lowercase.
    moonset = models.CharField(db_column='MoonSet', max_length=20)  # Field name made lowercase.
    lch = models.CharField(max_length=11)
    shv = models.CharField(max_length=11)
    clouds = models.CharField(max_length=11)
    wind_direction = models.CharField(max_length=40)
    wind_speed = models.CharField(max_length=20)
    wind_meter = models.CharField(max_length=20)
    drybulb = models.CharField(max_length=20)
    dew_point = models.CharField(max_length=20)
    station_level_p = models.CharField(max_length=20)
    sea_level_p = models.CharField(max_length=20)
    m_humidity = models.CharField(max_length=14)
    e_humidity = models.CharField(max_length=14)
    humidity = models.CharField(max_length=14)
    humidity_min = models.CharField(max_length=14)
    humidity_max = models.CharField(max_length=14)
    maximum_t = models.CharField(max_length=20)
    max_norm_def = models.CharField(max_length=20)
    min_norm_def = models.CharField(max_length=20)
    minimum_t = models.CharField(max_length=20)
    rainfall_00 = models.CharField(max_length=20)
    rainfall_06 = models.CharField(max_length=20)
    rainfall_12 = models.CharField(max_length=20)
    rainfall_18 = models.CharField(max_length=20)
    rainfall = models.CharField(max_length=20)
    rainfall_24 = models.CharField(max_length=20)
    rainfall_3 = models.CharField(max_length=20)
    rainfall_6 = models.CharField(max_length=20)
    lightning = models.CharField(max_length=20)
    thunder = models.CharField(max_length=20)
    fogg = models.CharField(max_length=20)
    rain = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'observe_data'
        unique_together = (('stcode', 'date_time'),)


class StationInfo(models.Model):
    st_code = models.IntegerField(blank=True, null=True)
    st_name = models.CharField(max_length=15, blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    lon = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station_info'


class StationObserved(models.Model):
    stationid = models.IntegerField(db_column='stationID', blank=True, null=True)  # Field name made lowercase.
    forecastdate = models.DateField(db_column='forecastDate', blank=True, null=True)  # Field name made lowercase.
    startstep = models.DateTimeField(db_column='startStep', blank=True, null=True)  # Field name made lowercase.
    endstep = models.DateTimeField(db_column='endStep', blank=True, null=True)  # Field name made lowercase.
    precipitation = models.CharField(max_length=50, blank=True, null=True)
    temperature = models.CharField(max_length=50, blank=True, null=True)
    relative_humidity = models.CharField(max_length=50, blank=True, null=True)
    dewpoint = models.CharField(max_length=50, blank=True, null=True)
    wind_speed = models.CharField(max_length=50, blank=True, null=True)
    wind_direction = models.CharField(max_length=50, blank=True, null=True)
    visibility = models.CharField(max_length=50, blank=True, null=True)
    total_cloud_cover = models.CharField(max_length=50, blank=True, null=True)
    station_level_pressure = models.CharField(max_length=50, blank=True, null=True)
    sea_level_pressure = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station_observed'


## Geo Django Models



# class WorldBorder(models.Model):
#     # Regular Django fields corresponding to the attributes in the
#     # world borders shapefile.
#     name = models.CharField(max_length=50)
#     area = models.IntegerField()
#     pop2005 = models.IntegerField('Population 2005')
#     fips = models.CharField('FIPS Code', max_length=2, null=True)
#     iso2 = models.CharField('2 Digit ISO', max_length=2)
#     iso3 = models.CharField('3 Digit ISO', max_length=3)
#     un = models.IntegerField('United Nations Code')
#     region = models.IntegerField('Region Code')
#     subregion = models.IntegerField('Sub-Region Code')
#     lon = models.FloatField()
#     lat = models.FloatField()

#     # GeoDjango-specific: a geometry field (MultiPolygonField)
#     mpoly = models.MultiPolygonField()

#     # Returns the string representation of the model.
#     def __str__(self):
#         return self.name

# class Shop(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.PointField()
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)

# class Country(models.Model):
#     name = models.CharField(max_length=50)
#     area = models.IntegerField()
#     pop2005 = models.IntegerField('Population 2005')
#     fips = models.CharField('FIPS Code', max_length=2, null=True)
#     iso2 = models.CharField('2 Digit ISO', max_length=2)
#     iso3 = models.CharField('3 Digit ISO', max_length=3)
#     un = models.IntegerField('United Nations Code')
#     region = models.IntegerField('Region Code')
#     subregion = models.IntegerField('Sub-Region Code')
#     lon = models.FloatField()
#     lat = models.FloatField()

#     # GeoDjango-specific: a geometry field (MultiPolygonField)
#     mpoly = models.MultiPolygonField()

#     # Returns the string representation of the model.
#     def __str__(self):
#         return self.name 

# class ModelFromRemoteTable1(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     country = models.CharField(max_length=200)
 
#     class Meta:
#         app_label = 'observed'
#         db_table = "BD_District_pr_day_ACCESS_CM2_ssp245_r1i1p1f1_2015_2100"
#         managed = False
 
#     def __str__(self):
#          return str(self.name)

