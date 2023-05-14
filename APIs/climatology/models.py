from django.contrib.gis.db import models

class Absoluteprovertymapbd(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    objectid = models.IntegerField(blank=True, null=True)
    count = models.FloatField(blank=True, null=True)
    first_dist = models.CharField(max_length=254, blank=True, null=True)
    first_than = models.CharField(max_length=254, blank=True, null=True)
    ave_divcod = models.FloatField(blank=True, null=True)
    div = models.IntegerField(blank=True, null=True)
    zl = models.IntegerField(blank=True, null=True)
    uz = models.IntegerField(blank=True, null=True)
    uzid = models.IntegerField(blank=True, null=True)
    geocode = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    upazila = models.CharField(max_length=254, blank=True, null=True)
    upper_pro = models.FloatField(blank=True, null=True)
    upper_poor = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AbsoluteProvertyMapBD'

class BdDistrictTasmaxDayAccessCm2Ssp245R1I1P1F120152100Dis(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    dist_name = models.CharField(db_column='Dist_name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_name_old = models.CharField(db_column='Dist_name_old', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dist_rimes = models.CharField(db_column='Dist_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_rimes_id = models.CharField(db_column='Dist_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_nc = models.CharField(db_column='Dist_nc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    div_rimes = models.CharField(db_column='Div_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    div_rimes_id = models.CharField(db_column='Div_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    station_name = models.CharField(max_length=8000, blank=True, null=True)
    value = models.CharField(max_length=8000, blank=True, null=True)
    year_2015 = models.FloatField(blank=True, null=True)
    year_2016 = models.FloatField(blank=True, null=True)
    year_2017 = models.FloatField(blank=True, null=True)
    year_2018 = models.FloatField(blank=True, null=True)
    year_2019 = models.FloatField(blank=True, null=True)
    year_2020 = models.FloatField(blank=True, null=True)
    year_2021 = models.FloatField(blank=True, null=True)
    year_2022 = models.FloatField(blank=True, null=True)
    year_2023 = models.FloatField(blank=True, null=True)
    year_2024 = models.FloatField(blank=True, null=True)
    year_2025 = models.FloatField(blank=True, null=True)
    year_2026 = models.FloatField(blank=True, null=True)
    year_2027 = models.FloatField(blank=True, null=True)
    year_2028 = models.FloatField(blank=True, null=True)
    year_2029 = models.FloatField(blank=True, null=True)
    year_2030 = models.FloatField(blank=True, null=True)
    year_2031 = models.FloatField(blank=True, null=True)
    year_2032 = models.FloatField(blank=True, null=True)
    year_2033 = models.FloatField(blank=True, null=True)
    year_2034 = models.FloatField(blank=True, null=True)
    year_2035 = models.FloatField(blank=True, null=True)
    year_2036 = models.FloatField(blank=True, null=True)
    year_2037 = models.FloatField(blank=True, null=True)
    year_2038 = models.FloatField(blank=True, null=True)
    year_2039 = models.FloatField(blank=True, null=True)
    year_2040 = models.FloatField(blank=True, null=True)
    year_2041 = models.FloatField(blank=True, null=True)
    year_2042 = models.FloatField(blank=True, null=True)
    year_2043 = models.FloatField(blank=True, null=True)
    year_2044 = models.FloatField(blank=True, null=True)
    year_2045 = models.FloatField(blank=True, null=True)
    year_2046 = models.FloatField(blank=True, null=True)
    year_2047 = models.FloatField(blank=True, null=True)
    year_2048 = models.FloatField(blank=True, null=True)
    year_2049 = models.FloatField(blank=True, null=True)
    year_2050 = models.FloatField(blank=True, null=True)
    year_2051 = models.FloatField(blank=True, null=True)
    year_2052 = models.FloatField(blank=True, null=True)
    year_2053 = models.FloatField(blank=True, null=True)
    year_2054 = models.FloatField(blank=True, null=True)
    year_2055 = models.FloatField(blank=True, null=True)
    year_2056 = models.FloatField(blank=True, null=True)
    year_2057 = models.FloatField(blank=True, null=True)
    year_2058 = models.FloatField(blank=True, null=True)
    year_2059 = models.FloatField(blank=True, null=True)
    year_2060 = models.FloatField(blank=True, null=True)
    year_2061 = models.FloatField(blank=True, null=True)
    year_2062 = models.FloatField(blank=True, null=True)
    year_2063 = models.FloatField(blank=True, null=True)
    year_2064 = models.FloatField(blank=True, null=True)
    year_2065 = models.FloatField(blank=True, null=True)
    year_2066 = models.FloatField(blank=True, null=True)
    year_2067 = models.FloatField(blank=True, null=True)
    year_2068 = models.FloatField(blank=True, null=True)
    year_2069 = models.FloatField(blank=True, null=True)
    year_2070 = models.FloatField(blank=True, null=True)
    year_2071 = models.FloatField(blank=True, null=True)
    year_2072 = models.FloatField(blank=True, null=True)
    year_2073 = models.FloatField(blank=True, null=True)
    year_2074 = models.FloatField(blank=True, null=True)
    year_2075 = models.FloatField(blank=True, null=True)
    year_2076 = models.FloatField(blank=True, null=True)
    year_2077 = models.FloatField(blank=True, null=True)
    year_2078 = models.FloatField(blank=True, null=True)
    year_2079 = models.FloatField(blank=True, null=True)
    year_2080 = models.FloatField(blank=True, null=True)
    year_2081 = models.FloatField(blank=True, null=True)
    year_2082 = models.FloatField(blank=True, null=True)
    year_2083 = models.FloatField(blank=True, null=True)
    year_2084 = models.FloatField(blank=True, null=True)
    year_2085 = models.FloatField(blank=True, null=True)
    year_2086 = models.FloatField(blank=True, null=True)
    year_2087 = models.FloatField(blank=True, null=True)
    year_2088 = models.FloatField(blank=True, null=True)
    year_2089 = models.FloatField(blank=True, null=True)
    year_2090 = models.FloatField(blank=True, null=True)
    year_2091 = models.FloatField(blank=True, null=True)
    year_2092 = models.FloatField(blank=True, null=True)
    year_2093 = models.FloatField(blank=True, null=True)
    year_2094 = models.FloatField(blank=True, null=True)
    year_2095 = models.FloatField(blank=True, null=True)
    year_2096 = models.FloatField(blank=True, null=True)
    year_2097 = models.FloatField(blank=True, null=True)
    year_2098 = models.FloatField(blank=True, null=True)
    year_2099 = models.FloatField(blank=True, null=True)
    year_2100 = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BD_District_tasmax_day_ACCESS_CM2_ssp245_r1i1p1f1_2015_2100_dis'


class BdDistrictTasmaxDayAccessCm2Ssp585R1I1P1F120152100Dis(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    dist_name = models.CharField(db_column='Dist_name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_name_old = models.CharField(db_column='Dist_name_old', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dist_rimes = models.CharField(db_column='Dist_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_rimes_id = models.CharField(db_column='Dist_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_nc = models.CharField(db_column='Dist_nc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    div_rimes = models.CharField(db_column='Div_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    div_rimes_id = models.CharField(db_column='Div_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    station_name = models.CharField(max_length=8000, blank=True, null=True)
    value = models.CharField(max_length=8000, blank=True, null=True)
    year_2015 = models.FloatField(blank=True, null=True)
    year_2016 = models.FloatField(blank=True, null=True)
    year_2017 = models.FloatField(blank=True, null=True)
    year_2018 = models.FloatField(blank=True, null=True)
    year_2019 = models.FloatField(blank=True, null=True)
    year_2020 = models.FloatField(blank=True, null=True)
    year_2021 = models.FloatField(blank=True, null=True)
    year_2022 = models.FloatField(blank=True, null=True)
    year_2023 = models.FloatField(blank=True, null=True)
    year_2024 = models.FloatField(blank=True, null=True)
    year_2025 = models.FloatField(blank=True, null=True)
    year_2026 = models.FloatField(blank=True, null=True)
    year_2027 = models.FloatField(blank=True, null=True)
    year_2028 = models.FloatField(blank=True, null=True)
    year_2029 = models.FloatField(blank=True, null=True)
    year_2030 = models.FloatField(blank=True, null=True)
    year_2031 = models.FloatField(blank=True, null=True)
    year_2032 = models.FloatField(blank=True, null=True)
    year_2033 = models.FloatField(blank=True, null=True)
    year_2034 = models.FloatField(blank=True, null=True)
    year_2035 = models.FloatField(blank=True, null=True)
    year_2036 = models.FloatField(blank=True, null=True)
    year_2037 = models.FloatField(blank=True, null=True)
    year_2038 = models.FloatField(blank=True, null=True)
    year_2039 = models.FloatField(blank=True, null=True)
    year_2040 = models.FloatField(blank=True, null=True)
    year_2041 = models.FloatField(blank=True, null=True)
    year_2042 = models.FloatField(blank=True, null=True)
    year_2043 = models.FloatField(blank=True, null=True)
    year_2044 = models.FloatField(blank=True, null=True)
    year_2045 = models.FloatField(blank=True, null=True)
    year_2046 = models.FloatField(blank=True, null=True)
    year_2047 = models.FloatField(blank=True, null=True)
    year_2048 = models.FloatField(blank=True, null=True)
    year_2049 = models.FloatField(blank=True, null=True)
    year_2050 = models.FloatField(blank=True, null=True)
    year_2051 = models.FloatField(blank=True, null=True)
    year_2052 = models.FloatField(blank=True, null=True)
    year_2053 = models.FloatField(blank=True, null=True)
    year_2054 = models.FloatField(blank=True, null=True)
    year_2055 = models.FloatField(blank=True, null=True)
    year_2056 = models.FloatField(blank=True, null=True)
    year_2057 = models.FloatField(blank=True, null=True)
    year_2058 = models.FloatField(blank=True, null=True)
    year_2059 = models.FloatField(blank=True, null=True)
    year_2060 = models.FloatField(blank=True, null=True)
    year_2061 = models.FloatField(blank=True, null=True)
    year_2062 = models.FloatField(blank=True, null=True)
    year_2063 = models.FloatField(blank=True, null=True)
    year_2064 = models.FloatField(blank=True, null=True)
    year_2065 = models.FloatField(blank=True, null=True)
    year_2066 = models.FloatField(blank=True, null=True)
    year_2067 = models.FloatField(blank=True, null=True)
    year_2068 = models.FloatField(blank=True, null=True)
    year_2069 = models.FloatField(blank=True, null=True)
    year_2070 = models.FloatField(blank=True, null=True)
    year_2071 = models.FloatField(blank=True, null=True)
    year_2072 = models.FloatField(blank=True, null=True)
    year_2073 = models.FloatField(blank=True, null=True)
    year_2074 = models.FloatField(blank=True, null=True)
    year_2075 = models.FloatField(blank=True, null=True)
    year_2076 = models.FloatField(blank=True, null=True)
    year_2077 = models.FloatField(blank=True, null=True)
    year_2078 = models.FloatField(blank=True, null=True)
    year_2079 = models.FloatField(blank=True, null=True)
    year_2080 = models.FloatField(blank=True, null=True)
    year_2081 = models.FloatField(blank=True, null=True)
    year_2082 = models.FloatField(blank=True, null=True)
    year_2083 = models.FloatField(blank=True, null=True)
    year_2084 = models.FloatField(blank=True, null=True)
    year_2085 = models.FloatField(blank=True, null=True)
    year_2086 = models.FloatField(blank=True, null=True)
    year_2087 = models.FloatField(blank=True, null=True)
    year_2088 = models.FloatField(blank=True, null=True)
    year_2089 = models.FloatField(blank=True, null=True)
    year_2090 = models.FloatField(blank=True, null=True)
    year_2091 = models.FloatField(blank=True, null=True)
    year_2092 = models.FloatField(blank=True, null=True)
    year_2093 = models.FloatField(blank=True, null=True)
    year_2094 = models.FloatField(blank=True, null=True)
    year_2095 = models.FloatField(blank=True, null=True)
    year_2096 = models.FloatField(blank=True, null=True)
    year_2097 = models.FloatField(blank=True, null=True)
    year_2098 = models.FloatField(blank=True, null=True)
    year_2099 = models.FloatField(blank=True, null=True)
    year_2100 = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BD_District_tasmax_day_ACCESS_CM2_ssp585_r1i1p1f1_2015_2100_dis'

class BdDistrictTasmaxDayBccCsm2MrSsp245R1I1P1F120152100(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    dist_name = models.CharField(db_column='Dist_name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_name_old = models.CharField(db_column='Dist_name_old', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dist_rimes = models.CharField(db_column='Dist_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_rimes_id = models.CharField(db_column='Dist_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_nc = models.CharField(db_column='Dist_nc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    div_rimes = models.CharField(db_column='Div_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    div_rimes_id = models.CharField(db_column='Div_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    station_name = models.CharField(max_length=8000, blank=True, null=True)
    value = models.CharField(max_length=8000, blank=True, null=True)
    year_2015 = models.FloatField(blank=True, null=True)
    year_2016 = models.FloatField(blank=True, null=True)
    year_2017 = models.FloatField(blank=True, null=True)
    year_2018 = models.FloatField(blank=True, null=True)
    year_2019 = models.FloatField(blank=True, null=True)
    year_2020 = models.FloatField(blank=True, null=True)
    year_2021 = models.FloatField(blank=True, null=True)
    year_2022 = models.FloatField(blank=True, null=True)
    year_2023 = models.FloatField(blank=True, null=True)
    year_2024 = models.FloatField(blank=True, null=True)
    year_2025 = models.FloatField(blank=True, null=True)
    year_2026 = models.FloatField(blank=True, null=True)
    year_2027 = models.FloatField(blank=True, null=True)
    year_2028 = models.FloatField(blank=True, null=True)
    year_2029 = models.FloatField(blank=True, null=True)
    year_2030 = models.FloatField(blank=True, null=True)
    year_2031 = models.FloatField(blank=True, null=True)
    year_2032 = models.FloatField(blank=True, null=True)
    year_2033 = models.FloatField(blank=True, null=True)
    year_2034 = models.FloatField(blank=True, null=True)
    year_2035 = models.FloatField(blank=True, null=True)
    year_2036 = models.FloatField(blank=True, null=True)
    year_2037 = models.FloatField(blank=True, null=True)
    year_2038 = models.FloatField(blank=True, null=True)
    year_2039 = models.FloatField(blank=True, null=True)
    year_2040 = models.FloatField(blank=True, null=True)
    year_2041 = models.FloatField(blank=True, null=True)
    year_2042 = models.FloatField(blank=True, null=True)
    year_2043 = models.FloatField(blank=True, null=True)
    year_2044 = models.FloatField(blank=True, null=True)
    year_2045 = models.FloatField(blank=True, null=True)
    year_2046 = models.FloatField(blank=True, null=True)
    year_2047 = models.FloatField(blank=True, null=True)
    year_2048 = models.FloatField(blank=True, null=True)
    year_2049 = models.FloatField(blank=True, null=True)
    year_2050 = models.FloatField(blank=True, null=True)
    year_2051 = models.FloatField(blank=True, null=True)
    year_2052 = models.FloatField(blank=True, null=True)
    year_2053 = models.FloatField(blank=True, null=True)
    year_2054 = models.FloatField(blank=True, null=True)
    year_2055 = models.FloatField(blank=True, null=True)
    year_2056 = models.FloatField(blank=True, null=True)
    year_2057 = models.FloatField(blank=True, null=True)
    year_2058 = models.FloatField(blank=True, null=True)
    year_2059 = models.FloatField(blank=True, null=True)
    year_2060 = models.FloatField(blank=True, null=True)
    year_2061 = models.FloatField(blank=True, null=True)
    year_2062 = models.FloatField(blank=True, null=True)
    year_2063 = models.FloatField(blank=True, null=True)
    year_2064 = models.FloatField(blank=True, null=True)
    year_2065 = models.FloatField(blank=True, null=True)
    year_2066 = models.FloatField(blank=True, null=True)
    year_2067 = models.FloatField(blank=True, null=True)
    year_2068 = models.FloatField(blank=True, null=True)
    year_2069 = models.FloatField(blank=True, null=True)
    year_2070 = models.FloatField(blank=True, null=True)
    year_2071 = models.FloatField(blank=True, null=True)
    year_2072 = models.FloatField(blank=True, null=True)
    year_2073 = models.FloatField(blank=True, null=True)
    year_2074 = models.FloatField(blank=True, null=True)
    year_2075 = models.FloatField(blank=True, null=True)
    year_2076 = models.FloatField(blank=True, null=True)
    year_2077 = models.FloatField(blank=True, null=True)
    year_2078 = models.FloatField(blank=True, null=True)
    year_2079 = models.FloatField(blank=True, null=True)
    year_2080 = models.FloatField(blank=True, null=True)
    year_2081 = models.FloatField(blank=True, null=True)
    year_2082 = models.FloatField(blank=True, null=True)
    year_2083 = models.FloatField(blank=True, null=True)
    year_2084 = models.FloatField(blank=True, null=True)
    year_2085 = models.FloatField(blank=True, null=True)
    year_2086 = models.FloatField(blank=True, null=True)
    year_2087 = models.FloatField(blank=True, null=True)
    year_2088 = models.FloatField(blank=True, null=True)
    year_2089 = models.FloatField(blank=True, null=True)
    year_2090 = models.FloatField(blank=True, null=True)
    year_2091 = models.FloatField(blank=True, null=True)
    year_2092 = models.FloatField(blank=True, null=True)
    year_2093 = models.FloatField(blank=True, null=True)
    year_2094 = models.FloatField(blank=True, null=True)
    year_2095 = models.FloatField(blank=True, null=True)
    year_2096 = models.FloatField(blank=True, null=True)
    year_2097 = models.FloatField(blank=True, null=True)
    year_2098 = models.FloatField(blank=True, null=True)
    year_2099 = models.FloatField(blank=True, null=True)
    year_2100 = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BD_District_tasmax_day_BCC_CSM2_MR_ssp245_r1i1p1f1_2015_2100'


class BdDistrictTasmaxDayBccCsm2MrSsp585R1I1P1F120152100(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    dist_name = models.CharField(db_column='Dist_name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_name_old = models.CharField(db_column='Dist_name_old', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dist_rimes = models.CharField(db_column='Dist_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_rimes_id = models.CharField(db_column='Dist_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_nc = models.CharField(db_column='Dist_nc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    div_rimes = models.CharField(db_column='Div_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    div_rimes_id = models.CharField(db_column='Div_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    station_name = models.CharField(max_length=8000, blank=True, null=True)
    value = models.CharField(max_length=8000, blank=True, null=True)
    year_2015 = models.FloatField(blank=True, null=True)
    year_2016 = models.FloatField(blank=True, null=True)
    year_2017 = models.FloatField(blank=True, null=True)
    year_2018 = models.FloatField(blank=True, null=True)
    year_2019 = models.FloatField(blank=True, null=True)
    year_2020 = models.FloatField(blank=True, null=True)
    year_2021 = models.FloatField(blank=True, null=True)
    year_2022 = models.FloatField(blank=True, null=True)
    year_2023 = models.FloatField(blank=True, null=True)
    year_2024 = models.FloatField(blank=True, null=True)
    year_2025 = models.FloatField(blank=True, null=True)
    year_2026 = models.FloatField(blank=True, null=True)
    year_2027 = models.FloatField(blank=True, null=True)
    year_2028 = models.FloatField(blank=True, null=True)
    year_2029 = models.FloatField(blank=True, null=True)
    year_2030 = models.FloatField(blank=True, null=True)
    year_2031 = models.FloatField(blank=True, null=True)
    year_2032 = models.FloatField(blank=True, null=True)
    year_2033 = models.FloatField(blank=True, null=True)
    year_2034 = models.FloatField(blank=True, null=True)
    year_2035 = models.FloatField(blank=True, null=True)
    year_2036 = models.FloatField(blank=True, null=True)
    year_2037 = models.FloatField(blank=True, null=True)
    year_2038 = models.FloatField(blank=True, null=True)
    year_2039 = models.FloatField(blank=True, null=True)
    year_2040 = models.FloatField(blank=True, null=True)
    year_2041 = models.FloatField(blank=True, null=True)
    year_2042 = models.FloatField(blank=True, null=True)
    year_2043 = models.FloatField(blank=True, null=True)
    year_2044 = models.FloatField(blank=True, null=True)
    year_2045 = models.FloatField(blank=True, null=True)
    year_2046 = models.FloatField(blank=True, null=True)
    year_2047 = models.FloatField(blank=True, null=True)
    year_2048 = models.FloatField(blank=True, null=True)
    year_2049 = models.FloatField(blank=True, null=True)
    year_2050 = models.FloatField(blank=True, null=True)
    year_2051 = models.FloatField(blank=True, null=True)
    year_2052 = models.FloatField(blank=True, null=True)
    year_2053 = models.FloatField(blank=True, null=True)
    year_2054 = models.FloatField(blank=True, null=True)
    year_2055 = models.FloatField(blank=True, null=True)
    year_2056 = models.FloatField(blank=True, null=True)
    year_2057 = models.FloatField(blank=True, null=True)
    year_2058 = models.FloatField(blank=True, null=True)
    year_2059 = models.FloatField(blank=True, null=True)
    year_2060 = models.FloatField(blank=True, null=True)
    year_2061 = models.FloatField(blank=True, null=True)
    year_2062 = models.FloatField(blank=True, null=True)
    year_2063 = models.FloatField(blank=True, null=True)
    year_2064 = models.FloatField(blank=True, null=True)
    year_2065 = models.FloatField(blank=True, null=True)
    year_2066 = models.FloatField(blank=True, null=True)
    year_2067 = models.FloatField(blank=True, null=True)
    year_2068 = models.FloatField(blank=True, null=True)
    year_2069 = models.FloatField(blank=True, null=True)
    year_2070 = models.FloatField(blank=True, null=True)
    year_2071 = models.FloatField(blank=True, null=True)
    year_2072 = models.FloatField(blank=True, null=True)
    year_2073 = models.FloatField(blank=True, null=True)
    year_2074 = models.FloatField(blank=True, null=True)
    year_2075 = models.FloatField(blank=True, null=True)
    year_2076 = models.FloatField(blank=True, null=True)
    year_2077 = models.FloatField(blank=True, null=True)
    year_2078 = models.FloatField(blank=True, null=True)
    year_2079 = models.FloatField(blank=True, null=True)
    year_2080 = models.FloatField(blank=True, null=True)
    year_2081 = models.FloatField(blank=True, null=True)
    year_2082 = models.FloatField(blank=True, null=True)
    year_2083 = models.FloatField(blank=True, null=True)
    year_2084 = models.FloatField(blank=True, null=True)
    year_2085 = models.FloatField(blank=True, null=True)
    year_2086 = models.FloatField(blank=True, null=True)
    year_2087 = models.FloatField(blank=True, null=True)
    year_2088 = models.FloatField(blank=True, null=True)
    year_2089 = models.FloatField(blank=True, null=True)
    year_2090 = models.FloatField(blank=True, null=True)
    year_2091 = models.FloatField(blank=True, null=True)
    year_2092 = models.FloatField(blank=True, null=True)
    year_2093 = models.FloatField(blank=True, null=True)
    year_2094 = models.FloatField(blank=True, null=True)
    year_2095 = models.FloatField(blank=True, null=True)
    year_2096 = models.FloatField(blank=True, null=True)
    year_2097 = models.FloatField(blank=True, null=True)
    year_2098 = models.FloatField(blank=True, null=True)
    year_2099 = models.FloatField(blank=True, null=True)
    year_2100 = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BD_District_tasmax_day_BCC_CSM2_MR_ssp585_r1i1p1f1_2015_2100'


class BdDistrictTasminDayAccessCm2Ssp245R1I1P1F120152100Dis(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    dist_name = models.CharField(db_column='Dist_name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_name_old = models.CharField(db_column='Dist_name_old', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dist_rimes = models.CharField(db_column='Dist_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_rimes_id = models.CharField(db_column='Dist_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_nc = models.CharField(db_column='Dist_nc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    div_rimes = models.CharField(db_column='Div_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    div_rimes_id = models.CharField(db_column='Div_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    station_name = models.CharField(max_length=8000, blank=True, null=True)
    value = models.CharField(max_length=8000, blank=True, null=True)
    year_2015 = models.FloatField(blank=True, null=True)
    year_2016 = models.FloatField(blank=True, null=True)
    year_2017 = models.FloatField(blank=True, null=True)
    year_2018 = models.FloatField(blank=True, null=True)
    year_2019 = models.FloatField(blank=True, null=True)
    year_2020 = models.FloatField(blank=True, null=True)
    year_2021 = models.FloatField(blank=True, null=True)
    year_2022 = models.FloatField(blank=True, null=True)
    year_2023 = models.FloatField(blank=True, null=True)
    year_2024 = models.FloatField(blank=True, null=True)
    year_2025 = models.FloatField(blank=True, null=True)
    year_2026 = models.FloatField(blank=True, null=True)
    year_2027 = models.FloatField(blank=True, null=True)
    year_2028 = models.FloatField(blank=True, null=True)
    year_2029 = models.FloatField(blank=True, null=True)
    year_2030 = models.FloatField(blank=True, null=True)
    year_2031 = models.FloatField(blank=True, null=True)
    year_2032 = models.FloatField(blank=True, null=True)
    year_2033 = models.FloatField(blank=True, null=True)
    year_2034 = models.FloatField(blank=True, null=True)
    year_2035 = models.FloatField(blank=True, null=True)
    year_2036 = models.FloatField(blank=True, null=True)
    year_2037 = models.FloatField(blank=True, null=True)
    year_2038 = models.FloatField(blank=True, null=True)
    year_2039 = models.FloatField(blank=True, null=True)
    year_2040 = models.FloatField(blank=True, null=True)
    year_2041 = models.FloatField(blank=True, null=True)
    year_2042 = models.FloatField(blank=True, null=True)
    year_2043 = models.FloatField(blank=True, null=True)
    year_2044 = models.FloatField(blank=True, null=True)
    year_2045 = models.FloatField(blank=True, null=True)
    year_2046 = models.FloatField(blank=True, null=True)
    year_2047 = models.FloatField(blank=True, null=True)
    year_2048 = models.FloatField(blank=True, null=True)
    year_2049 = models.FloatField(blank=True, null=True)
    year_2050 = models.FloatField(blank=True, null=True)
    year_2051 = models.FloatField(blank=True, null=True)
    year_2052 = models.FloatField(blank=True, null=True)
    year_2053 = models.FloatField(blank=True, null=True)
    year_2054 = models.FloatField(blank=True, null=True)
    year_2055 = models.FloatField(blank=True, null=True)
    year_2056 = models.FloatField(blank=True, null=True)
    year_2057 = models.FloatField(blank=True, null=True)
    year_2058 = models.FloatField(blank=True, null=True)
    year_2059 = models.FloatField(blank=True, null=True)
    year_2060 = models.FloatField(blank=True, null=True)
    year_2061 = models.FloatField(blank=True, null=True)
    year_2062 = models.FloatField(blank=True, null=True)
    year_2063 = models.FloatField(blank=True, null=True)
    year_2064 = models.FloatField(blank=True, null=True)
    year_2065 = models.FloatField(blank=True, null=True)
    year_2066 = models.FloatField(blank=True, null=True)
    year_2067 = models.FloatField(blank=True, null=True)
    year_2068 = models.FloatField(blank=True, null=True)
    year_2069 = models.FloatField(blank=True, null=True)
    year_2070 = models.FloatField(blank=True, null=True)
    year_2071 = models.FloatField(blank=True, null=True)
    year_2072 = models.FloatField(blank=True, null=True)
    year_2073 = models.FloatField(blank=True, null=True)
    year_2074 = models.FloatField(blank=True, null=True)
    year_2075 = models.FloatField(blank=True, null=True)
    year_2076 = models.FloatField(blank=True, null=True)
    year_2077 = models.FloatField(blank=True, null=True)
    year_2078 = models.FloatField(blank=True, null=True)
    year_2079 = models.FloatField(blank=True, null=True)
    year_2080 = models.FloatField(blank=True, null=True)
    year_2081 = models.FloatField(blank=True, null=True)
    year_2082 = models.FloatField(blank=True, null=True)
    year_2083 = models.FloatField(blank=True, null=True)
    year_2084 = models.FloatField(blank=True, null=True)
    year_2085 = models.FloatField(blank=True, null=True)
    year_2086 = models.FloatField(blank=True, null=True)
    year_2087 = models.FloatField(blank=True, null=True)
    year_2088 = models.FloatField(blank=True, null=True)
    year_2089 = models.FloatField(blank=True, null=True)
    year_2090 = models.FloatField(blank=True, null=True)
    year_2091 = models.FloatField(blank=True, null=True)
    year_2092 = models.FloatField(blank=True, null=True)
    year_2093 = models.FloatField(blank=True, null=True)
    year_2094 = models.FloatField(blank=True, null=True)
    year_2095 = models.FloatField(blank=True, null=True)
    year_2096 = models.FloatField(blank=True, null=True)
    year_2097 = models.FloatField(blank=True, null=True)
    year_2098 = models.FloatField(blank=True, null=True)
    year_2099 = models.FloatField(blank=True, null=True)
    year_2100 = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BD_District_tasmin_day_ACCESS_CM2_ssp245_r1i1p1f1_2015_2100_dis'


class BdDistrictTasminDayAccessCm2Ssp585R1I1P1F120152100Dis(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    dist_name = models.CharField(db_column='Dist_name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_name_old = models.CharField(db_column='Dist_name_old', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dist_rimes = models.CharField(db_column='Dist_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_rimes_id = models.CharField(db_column='Dist_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    dist_nc = models.CharField(db_column='Dist_nc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    div_rimes = models.CharField(db_column='Div_rimes', max_length=254, blank=True, null=True)  # Field name made lowercase.
    div_rimes_id = models.CharField(db_column='Div_rimes_id', max_length=254, blank=True, null=True)  # Field name made lowercase.
    station_name = models.CharField(max_length=8000, blank=True, null=True)
    value = models.CharField(max_length=8000, blank=True, null=True)
    year_2015 = models.FloatField(blank=True, null=True)
    year_2016 = models.FloatField(blank=True, null=True)
    year_2017 = models.FloatField(blank=True, null=True)
    year_2018 = models.FloatField(blank=True, null=True)
    year_2019 = models.FloatField(blank=True, null=True)
    year_2020 = models.FloatField(blank=True, null=True)
    year_2021 = models.FloatField(blank=True, null=True)
    year_2022 = models.FloatField(blank=True, null=True)
    year_2023 = models.FloatField(blank=True, null=True)
    year_2024 = models.FloatField(blank=True, null=True)
    year_2025 = models.FloatField(blank=True, null=True)
    year_2026 = models.FloatField(blank=True, null=True)
    year_2027 = models.FloatField(blank=True, null=True)
    year_2028 = models.FloatField(blank=True, null=True)
    year_2029 = models.FloatField(blank=True, null=True)
    year_2030 = models.FloatField(blank=True, null=True)
    year_2031 = models.FloatField(blank=True, null=True)
    year_2032 = models.FloatField(blank=True, null=True)
    year_2033 = models.FloatField(blank=True, null=True)
    year_2034 = models.FloatField(blank=True, null=True)
    year_2035 = models.FloatField(blank=True, null=True)
    year_2036 = models.FloatField(blank=True, null=True)
    year_2037 = models.FloatField(blank=True, null=True)
    year_2038 = models.FloatField(blank=True, null=True)
    year_2039 = models.FloatField(blank=True, null=True)
    year_2040 = models.FloatField(blank=True, null=True)
    year_2041 = models.FloatField(blank=True, null=True)
    year_2042 = models.FloatField(blank=True, null=True)
    year_2043 = models.FloatField(blank=True, null=True)
    year_2044 = models.FloatField(blank=True, null=True)
    year_2045 = models.FloatField(blank=True, null=True)
    year_2046 = models.FloatField(blank=True, null=True)
    year_2047 = models.FloatField(blank=True, null=True)
    year_2048 = models.FloatField(blank=True, null=True)
    year_2049 = models.FloatField(blank=True, null=True)
    year_2050 = models.FloatField(blank=True, null=True)
    year_2051 = models.FloatField(blank=True, null=True)
    year_2052 = models.FloatField(blank=True, null=True)
    year_2053 = models.FloatField(blank=True, null=True)
    year_2054 = models.FloatField(blank=True, null=True)
    year_2055 = models.FloatField(blank=True, null=True)
    year_2056 = models.FloatField(blank=True, null=True)
    year_2057 = models.FloatField(blank=True, null=True)
    year_2058 = models.FloatField(blank=True, null=True)
    year_2059 = models.FloatField(blank=True, null=True)
    year_2060 = models.FloatField(blank=True, null=True)
    year_2061 = models.FloatField(blank=True, null=True)
    year_2062 = models.FloatField(blank=True, null=True)
    year_2063 = models.FloatField(blank=True, null=True)
    year_2064 = models.FloatField(blank=True, null=True)
    year_2065 = models.FloatField(blank=True, null=True)
    year_2066 = models.FloatField(blank=True, null=True)
    year_2067 = models.FloatField(blank=True, null=True)
    year_2068 = models.FloatField(blank=True, null=True)
    year_2069 = models.FloatField(blank=True, null=True)
    year_2070 = models.FloatField(blank=True, null=True)
    year_2071 = models.FloatField(blank=True, null=True)
    year_2072 = models.FloatField(blank=True, null=True)
    year_2073 = models.FloatField(blank=True, null=True)
    year_2074 = models.FloatField(blank=True, null=True)
    year_2075 = models.FloatField(blank=True, null=True)
    year_2076 = models.FloatField(blank=True, null=True)
    year_2077 = models.FloatField(blank=True, null=True)
    year_2078 = models.FloatField(blank=True, null=True)
    year_2079 = models.FloatField(blank=True, null=True)
    year_2080 = models.FloatField(blank=True, null=True)
    year_2081 = models.FloatField(blank=True, null=True)
    year_2082 = models.FloatField(blank=True, null=True)
    year_2083 = models.FloatField(blank=True, null=True)
    year_2084 = models.FloatField(blank=True, null=True)
    year_2085 = models.FloatField(blank=True, null=True)
    year_2086 = models.FloatField(blank=True, null=True)
    year_2087 = models.FloatField(blank=True, null=True)
    year_2088 = models.FloatField(blank=True, null=True)
    year_2089 = models.FloatField(blank=True, null=True)
    year_2090 = models.FloatField(blank=True, null=True)
    year_2091 = models.FloatField(blank=True, null=True)
    year_2092 = models.FloatField(blank=True, null=True)
    year_2093 = models.FloatField(blank=True, null=True)
    year_2094 = models.FloatField(blank=True, null=True)
    year_2095 = models.FloatField(blank=True, null=True)
    year_2096 = models.FloatField(blank=True, null=True)
    year_2097 = models.FloatField(blank=True, null=True)
    year_2098 = models.FloatField(blank=True, null=True)
    year_2099 = models.FloatField(blank=True, null=True)
    year_2100 = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BD_District_tasmin_day_ACCESS_CM2_ssp585_r1i1p1f1_2015_2100_dis'


class Cycloneshelterbd(models.Model):
    geom = models.PointField(blank=True, null=True)
    div_id = models.CharField(max_length=254, blank=True, null=True)
    dist_id = models.CharField(max_length=254, blank=True, null=True)
    upz_id = models.CharField(max_length=254, blank=True, null=True)
    un_id = models.CharField(max_length=254, blank=True, null=True)
    un_uid = models.CharField(max_length=254, blank=True, null=True)
    divi_name = models.CharField(max_length=254, blank=True, null=True)
    dist_name = models.CharField(max_length=254, blank=True, null=True)
    upaz_name = models.CharField(max_length=254, blank=True, null=True)
    uni_name = models.CharField(max_length=254, blank=True, null=True)
    type_shelt = models.CharField(max_length=254, blank=True, null=True)
    shelternam = models.CharField(max_length=254, blank=True, null=True)
    mouza = models.CharField(max_length=254, blank=True, null=True)
    village = models.CharField(max_length=254, blank=True, null=True)
    distance_u = models.FloatField(blank=True, null=True)
    respperson = models.CharField(max_length=254, blank=True, null=True)
    constructe = models.CharField(max_length=254, blank=True, null=True)
    fundedby = models.CharField(max_length=254, blank=True, null=True)
    yearofcons = models.CharField(max_length=254, blank=True, null=True)
    structuret = models.CharField(max_length=254, blank=True, null=True)
    designtype = models.CharField(max_length=254, blank=True, null=True)
    floor_spac = models.FloatField(blank=True, null=True)
    nosfloor = models.FloatField(blank=True, null=True)
    capacity = models.FloatField(blank=True, null=True)
    toilet = models.CharField(max_length=254, blank=True, null=True)
    nooftoilet = models.FloatField(blank=True, null=True)
    separateto = models.CharField(max_length=254, blank=True, null=True)
    typeofuse = models.CharField(max_length=254, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CycloneShelterBD'


class Educationinstitutesbd(models.Model):
    geom = models.PointField(blank=True, null=True)
    objectid = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    new_id = models.CharField(max_length=254, blank=True, null=True)
    pathname = models.CharField(max_length=254, blank=True, null=True)
    division = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    upazila = models.CharField(max_length=254, blank=True, null=True)
    edutype = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EducationInstitutesBD'


class Extreanprovertymapbd(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    objectid = models.IntegerField(blank=True, null=True)
    count = models.FloatField(blank=True, null=True)
    first_dist = models.CharField(max_length=254, blank=True, null=True)
    first_than = models.CharField(max_length=254, blank=True, null=True)
    ave_divcod = models.FloatField(blank=True, null=True)
    div = models.IntegerField(blank=True, null=True)
    zl = models.IntegerField(blank=True, null=True)
    uz = models.IntegerField(blank=True, null=True)
    uzid = models.IntegerField(blank=True, null=True)
    geocode = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    upazila = models.CharField(max_length=254, blank=True, null=True)
    lower_pro = models.FloatField(blank=True, null=True)
    lower_poor = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExtreanProvertyMapBD'


class HydroriversV10As(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    hyriv_id = models.IntegerField(blank=True, null=True)
    next_down = models.IntegerField(blank=True, null=True)
    main_riv = models.IntegerField(blank=True, null=True)
    length_km = models.FloatField(blank=True, null=True)
    dist_dn_km = models.FloatField(blank=True, null=True)
    dist_up_km = models.FloatField(blank=True, null=True)
    catch_skm = models.FloatField(blank=True, null=True)
    upland_skm = models.FloatField(blank=True, null=True)
    endorheic = models.IntegerField(blank=True, null=True)
    dis_av_cms = models.FloatField(blank=True, null=True)
    ord_stra = models.IntegerField(blank=True, null=True)
    ord_clas = models.IntegerField(blank=True, null=True)
    ord_flow = models.IntegerField(blank=True, null=True)
    hybas_l12 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HydroRIVERS_v10_as'


class Internationalboundarybd(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    id_0 = models.IntegerField(blank=True, null=True)
    iso = models.CharField(max_length=254, blank=True, null=True)
    name_engli = models.CharField(max_length=254, blank=True, null=True)
    name_iso = models.CharField(max_length=254, blank=True, null=True)
    name_fao = models.CharField(max_length=254, blank=True, null=True)
    name_local = models.CharField(max_length=254, blank=True, null=True)
    name_obsol = models.CharField(max_length=254, blank=True, null=True)
    name_varia = models.CharField(max_length=254, blank=True, null=True)
    name_nonla = models.CharField(max_length=254, blank=True, null=True)
    name_frenc = models.CharField(max_length=254, blank=True, null=True)
    name_spani = models.CharField(max_length=254, blank=True, null=True)
    name_russi = models.CharField(max_length=254, blank=True, null=True)
    name_arabi = models.CharField(max_length=254, blank=True, null=True)
    name_chine = models.CharField(max_length=254, blank=True, null=True)
    waspartof = models.CharField(max_length=254, blank=True, null=True)
    contains = models.CharField(max_length=254, blank=True, null=True)
    sovereign = models.CharField(max_length=254, blank=True, null=True)
    iso2 = models.CharField(max_length=254, blank=True, null=True)
    www = models.CharField(max_length=254, blank=True, null=True)
    fips = models.CharField(max_length=254, blank=True, null=True)
    ison = models.FloatField(blank=True, null=True)
    validfr = models.CharField(max_length=254, blank=True, null=True)
    validto = models.CharField(max_length=254, blank=True, null=True)
    eumember = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InternationalBoundaryBD'


class Locationofindustries(models.Model):
    geom = models.PointField(blank=True, null=True)
    objectid = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    new_id = models.CharField(max_length=254, blank=True, null=True)
    pathname = models.CharField(max_length=254, blank=True, null=True)
    division = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    upazila = models.CharField(max_length=254, blank=True, null=True)
    ftype = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LocationOfIndustries'


class NepalOsmRoads(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    oneway = models.CharField(max_length=1, blank=True, null=True)
    maxspeed = models.IntegerField(blank=True, null=True)
    layer = models.BigIntegerField(blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)
    tunnel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Nepal_osm_roads'


class RegionClimdata(models.Model):
    geom = models.PointField(blank=True, null=True)
    recid = models.BigIntegerField(blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    stationnam = models.CharField(max_length=20, blank=True, null=True)
    sta_id = models.IntegerField(blank=True, null=True)
    altitude = models.BigIntegerField(blank=True, null=True)
    latdd = models.FloatField(blank=True, null=True)
    longdd = models.FloatField(blank=True, null=True)
    jan_tmax = models.FloatField(blank=True, null=True)
    feb_tmax = models.FloatField(blank=True, null=True)
    mar_tmax = models.FloatField(blank=True, null=True)
    apr_tmax = models.FloatField(blank=True, null=True)
    may_tmax = models.FloatField(blank=True, null=True)
    jun_tmax = models.FloatField(blank=True, null=True)
    jul_tmax = models.FloatField(blank=True, null=True)
    aug_tmax = models.FloatField(blank=True, null=True)
    sep_tmax = models.FloatField(blank=True, null=True)
    oct_tmax = models.FloatField(blank=True, null=True)
    nov_tmax = models.FloatField(blank=True, null=True)
    dec_tmax = models.FloatField(blank=True, null=True)
    jan_tmin = models.FloatField(blank=True, null=True)
    feb_tmin = models.FloatField(blank=True, null=True)
    mar_tmin = models.FloatField(blank=True, null=True)
    apr_tmin = models.FloatField(blank=True, null=True)
    may_tmin = models.FloatField(blank=True, null=True)
    jun_tmin = models.FloatField(blank=True, null=True)
    jul_tmin = models.FloatField(blank=True, null=True)
    aug_tmin = models.FloatField(blank=True, null=True)
    sep_tmin = models.FloatField(blank=True, null=True)
    oct_tmin = models.FloatField(blank=True, null=True)
    nov_tmin = models.FloatField(blank=True, null=True)
    dec_tmin = models.FloatField(blank=True, null=True)
    jan_pre = models.IntegerField(blank=True, null=True)
    feb_pre = models.IntegerField(blank=True, null=True)
    mar_pre = models.IntegerField(blank=True, null=True)
    apr_pre = models.IntegerField(blank=True, null=True)
    may_pre = models.IntegerField(blank=True, null=True)
    jun_pre = models.IntegerField(blank=True, null=True)
    jul_pre = models.IntegerField(blank=True, null=True)
    aug_pre = models.IntegerField(blank=True, null=True)
    sep_pre = models.IntegerField(blank=True, null=True)
    oct_pre = models.IntegerField(blank=True, null=True)
    nov_pre = models.IntegerField(blank=True, null=True)
    dec_pre = models.IntegerField(blank=True, null=True)
    jan_hum = models.FloatField(blank=True, null=True)
    feb_hum = models.FloatField(blank=True, null=True)
    mar_hum = models.FloatField(blank=True, null=True)
    apr_hum = models.FloatField(blank=True, null=True)
    may_hum = models.FloatField(blank=True, null=True)
    jun_hum = models.FloatField(blank=True, null=True)
    jul_hum = models.FloatField(blank=True, null=True)
    aug_hum = models.FloatField(blank=True, null=True)
    sep_hum = models.FloatField(blank=True, null=True)
    oct_hum = models.FloatField(blank=True, null=True)
    nov_hum = models.FloatField(blank=True, null=True)
    dec_hum = models.FloatField(blank=True, null=True)
    jan_bss = models.FloatField(blank=True, null=True)
    feb_bss = models.FloatField(blank=True, null=True)
    mar_bss = models.FloatField(blank=True, null=True)
    apr_bss = models.FloatField(blank=True, null=True)
    may_bss = models.FloatField(blank=True, null=True)
    jun_bss = models.FloatField(blank=True, null=True)
    jul_bss = models.FloatField(blank=True, null=True)
    aug_bss = models.FloatField(blank=True, null=True)
    sep_bss = models.FloatField(blank=True, null=True)
    oct_bss = models.FloatField(blank=True, null=True)
    nov_bss = models.FloatField(blank=True, null=True)
    dec_bss = models.FloatField(blank=True, null=True)
    jan_ws = models.FloatField(blank=True, null=True)
    feb_ws = models.FloatField(blank=True, null=True)
    mar_ws = models.FloatField(blank=True, null=True)
    apr_ws = models.FloatField(blank=True, null=True)
    may_ws = models.FloatField(blank=True, null=True)
    jun_ws = models.FloatField(blank=True, null=True)
    jul_ws = models.FloatField(blank=True, null=True)
    aug_ws = models.FloatField(blank=True, null=True)
    sep_ws = models.FloatField(blank=True, null=True)
    oct_ws = models.FloatField(blank=True, null=True)
    nov_ws = models.FloatField(blank=True, null=True)
    dec_ws = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Region_Climdata'


class SriLankaOsmRoads(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    oneway = models.CharField(max_length=1, blank=True, null=True)
    maxspeed = models.IntegerField(blank=True, null=True)
    layer = models.BigIntegerField(blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)
    tunnel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sri_Lanka_osm_roads'


class AdminToolsDashboardPreferences(models.Model):
    data = models.TextField()
    dashboard_id = models.CharField(max_length=100)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin_tools_dashboard_preferences'
        unique_together = (('user', 'dashboard_id'),)


class AdminToolsMenuBookmark(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin_tools_menu_bookmark'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class BtclFiberOpticNetworkConnectedUnionsbd(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    unioncod01 = models.FloatField(blank=True, null=True)
    divname = models.CharField(max_length=254, blank=True, null=True)
    distname = models.CharField(max_length=254, blank=True, null=True)
    thaname = models.CharField(max_length=254, blank=True, null=True)
    uniname = models.CharField(max_length=254, blank=True, null=True)
    remarks = models.CharField(max_length=254, blank=True, null=True)
    landtype = models.CharField(max_length=254, blank=True, null=True)
    uni_name_u = models.CharField(max_length=254, blank=True, null=True)
    ucode_updt = models.CharField(max_length=254, blank=True, null=True)
    fid_1 = models.FloatField(blank=True, null=True)
    connect = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'btcl_fiber_optic_network_connected_unionsBD'


class DemographyPoly(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    recid = models.BigIntegerField(blank=True, null=True)
    dis_code = models.IntegerField(blank=True, null=True)
    dist_name = models.CharField(max_length=30, blank=True, null=True)
    divcode = models.IntegerField(blank=True, null=True)
    disdiv = models.IntegerField(blank=True, null=True)
    districtco = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=13, blank=True, null=True)
    ch_dr97 = models.FloatField(blank=True, null=True)
    ch_dr98 = models.FloatField(blank=True, null=True)
    ch_dr2002 = models.FloatField(blank=True, null=True)
    ch_br2000 = models.FloatField(blank=True, null=True)
    ch_br2001 = models.FloatField(blank=True, null=True)
    ch_br2002 = models.FloatField(blank=True, null=True)
    crud_dr200 = models.FloatField(blank=True, null=True)
    crud_dr201 = models.FloatField(blank=True, null=True)
    crud_dr202 = models.FloatField(blank=True, null=True)
    inf_mr2000 = models.FloatField(blank=True, null=True)
    inf_mr2001 = models.FloatField(blank=True, null=True)
    inf_mr2002 = models.FloatField(blank=True, null=True)
    tot_fr2000 = models.FloatField(blank=True, null=True)
    tot_fr2001 = models.FloatField(blank=True, null=True)
    tot_fr2002 = models.FloatField(blank=True, null=True)
    zbi_crud_2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demography_poly'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class GisOsmBuildingsAFree1(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_buildings_a_free_1'


class GisOsmLanduseAFree1(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_landuse_a_free_1'


class GisOsmNaturalAFree1(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_natural_a_free_1'


class GisOsmNaturalFree1(models.Model):
    geom = models.PointField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_natural_free_1'


class GisOsmPlacesAFree1(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_places_a_free_1'


class GisOsmPlacesFree1(models.Model):
    geom = models.PointField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_places_free_1'


class GisOsmPofwAFree1(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_pofw_a_free_1'


class GisOsmPofwFree1(models.Model):
    geom = models.PointField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_pofw_free_1'


class GisOsmPoisAFree1(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_pois_a_free_1'


class GisOsmPoisFree1(models.Model):
    geom = models.PointField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_pois_free_1'


class GisOsmRailwaysFree1(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    layer = models.BigIntegerField(blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)
    tunnel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_railways_free_1'


class GisOsmRoadsFree1(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    oneway = models.CharField(max_length=1, blank=True, null=True)
    maxspeed = models.IntegerField(blank=True, null=True)
    layer = models.BigIntegerField(blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)
    tunnel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_roads_free_1'


class GisOsmTrafficAFree1(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_traffic_a_free_1'


class GisOsmTrafficFree1(models.Model):
    geom = models.PointField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_traffic_free_1'


class GisOsmTransportAFree1(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_transport_a_free_1'


class GisOsmTransportFree1(models.Model):
    geom = models.PointField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_transport_free_1'


class GisOsmWaterAFree1(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_water_a_free_1'


class GisOsmWaterwaysFree1(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_osm_waterways_free_1'


class Landtype(models.Model):
    id_0 = models.AutoField(primary_key=True)
    id = models.BigIntegerField(blank=True, null=True)
    gridcode = models.BigIntegerField(blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'landtype'
# Unable to inspect table 'us_gaz'
# The error was: permission denied for table us_gaz
# Unable to inspect table 'us_lex'
# The error was: permission denied for table us_lex
# Unable to inspect table 'us_rules'
# The error was: permission denied for table us_rules
