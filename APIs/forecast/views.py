from rest_framework import permissions,viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from forecast.models import ApisUpazila,ApisUpazilaForecastDaily,ApisUpazilaForecastSteps
from forecast.serializers import dailyForecastSerializer,hourlyForecastSerializer,upazilaSerializer

from forecast.scripts.generateWeatherData import returnForecastDate, returnDailyWeather,returnDailyMaxMin


from django_filters.rest_framework import DjangoFilterBackend

from datetime import date, datetime, timedelta
from django_pandas.io import read_frame 

import pandas as pd


@api_view(['GET'])
def forecastFromUrl(request,  **kwargs):

    category=kwargs['category']
    thisParameter=kwargs['parameter']

    if category=='districts':
        forecastDate=returnForecastDate(1)
        thisParametert=kwargs['parameter']

        if thisParameter=='daily':
            dailyWeather,tenDaysWeather=returnDailyWeather(f'{forecastDate}')

    responseValue=dailyWeather

    return Response(responseValue)

@api_view(['GET'])
def dailyMaxMin(request,  **kwargs):

    category=kwargs['category']
    thisParameter=kwargs['parameter']

    if category=='daily':
        forecastDate=returnForecastDate(1)
        thisParametert=kwargs['parameter']

        if thisParameter=='max-min':
            maxMinList=returnDailyMaxMin(forecastDate)

    responseValue=maxMinList

    return Response(responseValue)

