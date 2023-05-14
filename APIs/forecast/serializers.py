from rest_framework import serializers
from rest_framework.serializers import Serializer,FileField

from forecast.models import ApisUpazilaForecastDaily,ApisUpazilaForecastSteps,ApisUpazila
from pagination import LargeResultsSetPagination,StandardResultsSetPagination


class upazilaSerializer(serializers.ModelSerializer):

    class Meta:

        model=ApisUpazila
        fields=['id','adm3_pcode','name','adm2_pcode','district']

        pagination_class = LargeResultsSetPagination

class dailyForecastSerializer(serializers.ModelSerializer):

    # upazila=upazilaSerializer()
    adm3_pcode=serializers.SerializerMethodField()
    name=serializers.SerializerMethodField()

    def get_adm3_pcode(self,ApisUpazilaForecastDaily):
        adm3_pcode = ApisUpazila.objects.filter(id=ApisUpazilaForecastDaily.upazila_id).values_list('adm3_pcode', flat=True)[0]
        return adm3_pcode
    
    def get_name(self,ApisUpazilaForecastDaily):
        name = ApisUpazila.objects.filter(id=ApisUpazilaForecastDaily.upazila_id).values_list('name', flat=True)[0]
        return name

    class Meta:

        model= ApisUpazilaForecastDaily
        fields=['parameter_id','upazila_id','adm3_pcode','name','forecast_date','step_start','step_end','val_min','val_avg','val_max']

        pagination_class = LargeResultsSetPagination

class hourlyForecastSerializer(serializers.ModelSerializer):

    class Meta:
        
        model=ApisUpazilaForecastSteps
        fields=['upazila_id','parameter_id','forecast_date','step_start','step_end','val_min','val_avg','val_max']

        pagination_class = LargeResultsSetPagination

