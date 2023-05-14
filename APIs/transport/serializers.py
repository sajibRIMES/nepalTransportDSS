from rest_framework import serializers
from rest_framework.serializers import Serializer,FileField

from transport.models import LgedRoad
from pagination import LargeResultsSetPagination,StandardResultsSetPagination

class lgedRoadSerializer(serializers.ModelSerializer):

    class Meta:

        model=LgedRoad
        fields=['rdname','dist_id','dist_name']
        pagination_class = LargeResultsSetPagination