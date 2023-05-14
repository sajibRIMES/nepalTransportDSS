from django.shortcuts import render
from rest_framework import permissions,viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import FileResponse,JsonResponse

from observedClimatology.models import Table19812021Tmax
from observedClimatology.serializers import tmaxSerializer
from rest_framework import serializers

import json
import geojson

from django.contrib.gis.geos import GEOSGeometry


class tmaxViewSet(viewsets.ModelViewSet):
    
    queryset=Table19812021Tmax.objects.all()
    serializer_class=tmaxSerializer

