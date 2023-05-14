from django.shortcuts import render
from rest_framework import permissions,viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import FileResponse,JsonResponse

from transport.models import LgedRoad
from transport.serializers import lgedRoadSerializer
from rest_framework import serializers

import json
import geojson

from django.contrib.gis.geos import GEOSGeometry


class lgedRoadViewSet(viewsets.ModelViewSet):
    
    queryset=LgedRoad.objects.all()
    
    serializer_class=lgedRoadSerializer


class bdRoadViewSet(viewsets.ViewSet):

    def list(self, request):
        with open('/Volumes/dssDevelopment/djangular/APIs/transport/nationalGeoRoads.geojson', 'r') as f:
            gj = geojson.load(f)
            thisJson=json.dumps(gj)

        thisJson=gj['features']
        
        return Response(thisJson)

