from rest_framework import serializers
from rest_framework.serializers import Serializer,FileField

from observedClimatology.models import Table19812021Tmax
from pagination import LargeResultsSetPagination,StandardResultsSetPagination

class tmaxSerializer(serializers.ModelSerializer):

    class Meta:

        model=Table19812021Tmax
        fields=['month','region','temp']
        pagination_class = LargeResultsSetPagination