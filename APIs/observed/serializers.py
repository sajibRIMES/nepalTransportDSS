from rest_framework import serializers
from rest_framework.serializers import Serializer,FileField

from django.contrib.auth.models import User, Group
from observed.models import StationInfo, ObserveData, StationObserved
from pagination import LargeResultsSetPagination,StandardResultsSetPagination


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


## Upload Serializer
class uploadSerializer(serializers.Serializer):
    
    file_uploaded=serializers.FileField()
   
    # file_uploaded1=serializers.FileField()
    # file_uploaded2=serializers.FileField()
    
    class Meta:
        fields=['file_uploaded']



class StationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=StationInfo
        fields=['st_code','st_name','lat','lon']
        pagination_class = LargeResultsSetPagination

        

class observedSerializer(serializers.ModelSerializer):

    st_name=serializers.SerializerMethodField()

    def get_st_name(self,ObserveData):
        st_name = StationInfo.objects.filter(st_code=ObserveData.stcode).values_list('st_name', flat=True)[0]
        return st_name

    class Meta:

        model = ObserveData

        fields=[
            'stcode','st_name','date_time','maximum_t','minimum_t','humidity_max','humidity_min','rain',
            'wind_speed','clouds','station_level_p','sea_level_p','lightning','thunder','fogg'
            ]

        pagination_class = StandardResultsSetPagination

class stationObservedSerializer(serializers.ModelSerializer):
    
    # print(StationInfo.objects.filter(st_code=StationObserved.stationid))

    st_name=serializers.SerializerMethodField()
    # serializers.DateField(format="%Y-%m-%d")
    def to_representation(self, instance):
        representation = super(stationObservedSerializer, self).to_representation(instance)
        representation['startstep'] = instance.startstep.strftime("%H:%M:%S")
        representation['endstep'] = instance.endstep.strftime("%H:%M:%S")
        return representation

    def get_st_name(self,StationObserved):
        st_name = StationInfo.objects.filter(st_code=StationObserved.stationid).values_list('st_name', flat=True)
        return st_name
    

    class Meta:
        model= StationObserved

        fields=[
            'stationid','st_name','forecastdate','startstep','endstep','precipitation','temperature',
            'relative_humidity','dewpoint','wind_speed','visibility','station_level_pressure','sea_level_pressure'
        ]

        pagination_class = StandardResultsSetPagination

# class figureSerializer()

