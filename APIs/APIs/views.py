from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def home(request):

    context={
        
        'nepal-forecast':'http://127.0.0.1:8000/forecast/forecast-from-url/districts/daily/',
        'nepal-daily-max-min':'http://127.0.0.1:8000/forecast/day-max-min/daily/max-min/',
        # 'forecast':'http://127.0.0.1:8000/forecast/',
        # 'observed':'http://127.0.0.1:8000/observed/',
        # 'observedClimatology':'http://127.0.0.1:8000/observedClimatology/',
        # 'climatology':'http://127.0.0.1:8000/climatology/',
        # 'transport':'http://127.0.0.1:8000/transport/'

        # '1':'http://127.0.0.1:8000/figureByParameter/1'
        
        }
        
    return Response(context)