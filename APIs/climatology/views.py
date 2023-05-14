from django.shortcuts import render
from rest_framework import permissions,viewsets, generics
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from climatology.models import Absoluteprovertymapbd,BdDistrictTasmaxDayAccessCm2Ssp245R1I1P1F120152100Dis
from climatology.serializers import provertySerializer,climateSerializer

def climateIndex(request):
    return render(request, 'climateIndex.html')

class provertyViewSet(viewsets.ModelViewSet):
    
    queryset = Absoluteprovertymapbd.objects.all()
    # queryset=queryset.filter(st_code=41923)
    serializer_class = provertySerializer

class climateViewSet(viewsets.ModelViewSet):
    queryset=BdDistrictTasmaxDayAccessCm2Ssp245R1I1P1F120152100Dis.objects.all()
    serializer_class=climateSerializer
