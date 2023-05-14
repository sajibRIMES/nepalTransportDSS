# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class BdBiwtaTerminal(models.Model):
    id_0 = models.IntegerField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    locid = models.BigIntegerField(blank=True, null=True)
    locname = models.CharField(max_length=15, blank=True, null=True)
    fclass = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=28, blank=True, null=True)
    btmlong = models.FloatField(blank=True, null=True)
    btmlat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BD_BIWTA terminal'


class BdRoadsNzr(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    length = models.FloatField(blank=True, null=True)
    rd_nr = models.CharField(max_length=6, blank=True, null=True)
    start = models.CharField(max_length=30, blank=True, null=True)
    end = models.CharField(max_length=30, blank=True, null=True)
    rd_class = models.FloatField(blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    shape_leng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BD_Roads_NZR'


class BdRoadsWgs84(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    objectid = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    rd_nr = models.CharField(max_length=6, blank=True, null=True)
    start = models.CharField(max_length=30, blank=True, null=True)
    end = models.CharField(max_length=30, blank=True, null=True)
    rd_class = models.FloatField(blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    shape_leng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BD_Roads_WGS84'


class BdPolder(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    area = models.FloatField(blank=True, null=True)
    scode = models.BigIntegerField(blank=True, null=True)
    zone = models.CharField(max_length=254, blank=True, null=True)
    sname = models.CharField(max_length=254, blank=True, null=True)
    newtype = models.CharField(max_length=254, blank=True, null=True)
    typecode = models.CharField(max_length=254, blank=True, null=True)
    parea = models.FloatField(blank=True, null=True)
    ystart = models.CharField(max_length=254, blank=True, null=True)
    ycompl = models.CharField(max_length=254, blank=True, null=True)
    value = models.CharField(max_length=254, blank=True, null=True)
    circle = models.CharField(max_length=30, blank=True, null=True)
    source = models.CharField(max_length=25, blank=True, null=True)
    area_ha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BD_polder'


class Ferry(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    area = models.FloatField(blank=True, null=True)
    perimeter = models.FloatField(blank=True, null=True)
    rhd_fry_field = models.BigIntegerField(db_column='rhd_fry_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rhd_fry_id = models.BigIntegerField(blank=True, null=True)
    location = models.CharField(max_length=40, blank=True, null=True)
    f_polygoni = models.BigIntegerField(blank=True, null=True)
    f_scale = models.FloatField(blank=True, null=True)
    f_angle = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ferry'


class ImportantLocation(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    area = models.FloatField(blank=True, null=True)
    perimeter = models.FloatField(blank=True, null=True)
    rds_loc_field = models.BigIntegerField(db_column='rds_loc_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rds_loc_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    f_polygoni = models.BigIntegerField(blank=True, null=True)
    f_scale = models.FloatField(blank=True, null=True)
    f_angle = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Important_Location'


class LgedRoad(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    rdname = models.CharField(max_length=150, blank=True, null=True)
    crestwidth = models.FloatField(blank=True, null=True)
    mrva_type = models.CharField(max_length=50, blank=True, null=True)
    mrva_b_typ = models.CharField(max_length=50, blank=True, null=True)
    length_rd = models.FloatField(blank=True, null=True)
    div_id = models.CharField(max_length=10, blank=True, null=True)
    dist_id = models.CharField(max_length=10, blank=True, null=True)
    upz_id_1 = models.CharField(max_length=10, blank=True, null=True)
    un_id = models.CharField(max_length=10, blank=True, null=True)
    un_uid = models.CharField(max_length=20, blank=True, null=True)
    divi_name = models.CharField(max_length=50, blank=True, null=True)
    dist_name = models.CharField(max_length=50, blank=True, null=True)
    upaz_name = models.CharField(max_length=50, blank=True, null=True)
    uni_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LGED_Road'


class RhdRoad(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    length = models.FloatField(blank=True, null=True)
    rhd_rds_field = models.IntegerField(db_column='rhd_rds_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rhd_rds_id = models.IntegerField(blank=True, null=True)
    gisroad_id = models.FloatField(blank=True, null=True)
    rd_nr = models.CharField(max_length=6, blank=True, null=True)
    start = models.CharField(max_length=30, blank=True, null=True)
    end = models.CharField(max_length=30, blank=True, null=True)
    roadlength = models.FloatField(blank=True, null=True)
    rd_class = models.FloatField(blank=True, null=True)
    meter = models.FloatField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    drivetime = models.FloatField(blank=True, null=True)
    linesegs = models.IntegerField(blank=True, null=True)
    fracdim = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RHD_Road'


class Railways(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    fnode_field = models.BigIntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    tnode_field = models.BigIntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.BigIntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.BigIntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    length = models.FloatField(blank=True, null=True)
    bd_rly_field = models.BigIntegerField(db_column='bd_rly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    bd_rly_id = models.BigIntegerField(blank=True, null=True)
    type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Railways'


class RiverSea(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    area = models.FloatField(blank=True, null=True)
    perimeter = models.FloatField(blank=True, null=True)
    bd_riv_field = models.BigIntegerField(db_column='bd_riv_', blank=True, null=True)  # Field renamed because it ended with '_'.
    bd_riv_id = models.BigIntegerField(blank=True, null=True)
    type = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'River_Sea'


class RoadLgedBd(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    rdname = models.CharField(max_length=150, blank=True, null=True)
    crestwidth = models.FloatField(blank=True, null=True)
    mrva_type = models.CharField(max_length=50, blank=True, null=True)
    mrva_b_typ = models.CharField(max_length=50, blank=True, null=True)
    length_rd = models.FloatField(blank=True, null=True)
    div_id = models.CharField(max_length=10, blank=True, null=True)
    dist_id = models.CharField(max_length=10, blank=True, null=True)
    upz_id_1 = models.CharField(max_length=10, blank=True, null=True)
    un_id = models.CharField(max_length=10, blank=True, null=True)
    un_uid = models.CharField(max_length=20, blank=True, null=True)
    divi_name = models.CharField(max_length=50, blank=True, null=True)
    dist_name = models.CharField(max_length=50, blank=True, null=True)
    upaz_name = models.CharField(max_length=50, blank=True, null=True)
    uni_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Road_LGED_BD'


class RoadNetworkOsm(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    oneway = models.CharField(max_length=1, blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)
    tunnel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Road_Network_OSM'


class Waterways(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=48, blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'waterways'
