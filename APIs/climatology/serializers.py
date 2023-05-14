from rest_framework import serializers
from rest_framework.serializers import Serializer,FileField
from django.contrib.auth.models import User, Group
from pagination import LargeResultsSetPagination,StandardResultsSetPagination

from climatology.models import Absoluteprovertymapbd,BdDistrictTasmaxDayAccessCm2Ssp245R1I1P1F120152100Dis

class provertySerializer(serializers.ModelSerializer):
    class Meta:
        model=Absoluteprovertymapbd
        fields=['geocode','upazila','upper_pro','upper_poor','geom']
        pagination_class = LargeResultsSetPagination

class climateSerializer(serializers.ModelSerializer):
    class Meta:
        model=BdDistrictTasmaxDayAccessCm2Ssp245R1I1P1F120152100Dis
        fields=['dist_name','dist_name_old','dist_rimes','station_name','value','year_2015','geom']
        parination_class=LargeResultsSetPagination

# class observedSerializer(serializers.ModelSerializer):

#     st_name=serializers.SerializerMethodField()

#     def get_st_name(self,ObserveData):
#         st_name = StationInfo.objects.filter(st_code=ObserveData.stcode).values_list('st_name', flat=True)[0]
#         return st_name

#     class Meta:

#         model = ObserveData

#         fields=[
#             'stcode','st_name','date_time','maximum_t','minimum_t','humidity_max','humidity_min','rain',
#             'wind_speed','clouds','station_level_p','sea_level_p','lightning','thunder','fogg'
#             ]

#         pagination_class = StandardResultsSetPagination

