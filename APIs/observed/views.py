from rest_framework import permissions,viewsets, generics
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt
# from django.test  import TransactionTestCase

from django.contrib.auth.models import User, Group

from observed.models import  StationInfo,ObserveData,StationObserved
from observed.serializers import UserSerializer, GroupSerializer,StationInfoSerializer,observedSerializer,stationObservedSerializer,uploadSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from subprocess import Popen
from observed.scripts.generateFigure import initializeFigure

from observed.scripts.observedClimatology import returnEnacts
from observed.scripts.worldCover import worldCoverFigure
from observed.scripts.geoData import mapInitialize,returnRoadGeoDataframes

from observed.scripts.emission import returnEmissionJson,returnDistrictEmission, returnPlotly,returnDistrictLanCover,returnDistrictFMD,returnLivestockPopulation,returnDistrictCWD
from observed.scripts.emission import returnCorrelationDF

import json
from bokeh.embed import json_item

from datetime import date, datetime, timedelta
import folium
import geemap

import csv,io



from django.shortcuts import render
import sys
from pathlib import Path
import os
from subprocess import run,PIPE


import geopandas as gpd


BASE_DIR = Path(__file__).resolve().parent.parent


observedDate=datetime.today()-timedelta(days=1)
dateInput=datetime.strftime(observedDate,'%Y-%m-%d')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

## File Upload View
class uploadViewSet(viewsets.ViewSet):
    
    serializer_class=uploadSerializer

    # file.name           # Gives name
    # file.content_type   # Gives Content type text/html etc
    # file.size           # Gives file's size in byte
    # file.read()         # Reads file

    def shapeToJson(self,fileName):

        fileText=io.TextIOWrapper(fileName)


        return fileText

    def handle_csv_data(self,csv_file):

        csv_file = io.TextIOWrapper(csv_file)  # python 3 only
        dialect = csv.Sniffer().sniff(csv_file.read(1024), delimiters=";,")
        csv_file.seek(0)
        reader = csv.reader(csv_file, dialect)
        return list(reader)

    def list(self,request):
        return Response("Get API")

    def handle_uploaded_file(self,f):

        with open('/Volumes/dssDevelopment/djangular/APIs/observed/files' + f.name,'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def create(self,request):
        

        # csv_file = request.FILES['file_uploaded'].file
        # csv_content = self.handle_csv_data(csv_file) 
        # response=json.dumps(csv_content)

        thisFile = request.FILES['file_uploaded']
        # self.handle_uploaded_file(thisFile)

        # self.handle_uploaded_file(thisFile)
        # thatFile = request.FILES['file_uploaded2']
        # self.handle_uploaded_file(thatFile)

        # thisFile = request.FILES.getlist('file_uploaded')

        # fileDict={}
        # for f in thisFile:
        #     fileDict['name']=f.name



        
        # reading=thisFile.read()
        # fileContent = self.shapeToJson(thisFile)

        # context1={
        #     'name':thisFile.name,
        #     'content_type':thisFile.content_type,
        #     'size':thisFile.size,
        #     'charset':thisFile.charset,
        #     'filePath':thisFile.temporary_file_path()
        # }

        # context2={
        #     'name':thatFile.name,
        #     'content_type':thatFile.content_type,
        #     'size':thatFile.size,
        #     'charset':thatFile.charset,
        #     'filePath':thatFile.temporary_file_path()
        # }

        # context={'file1':context1,'file2':context2}

        context={
            'name':thisFile.name,
            'content_type':thisFile.content_type,
            'size':thisFile.size,
            'charset':thisFile.charset,
            'filePath':thisFile.temporary_file_path()
        }
        shapePath=context['filePath']
        # districtsDF=gpd.read_file(shapePath)

        response=context
        # response=json.dumps(fileContent)

        # file_uploaded = request.FILES.get('file_uploaded')

        # content_type = file_uploaded.content_type
        
        # response = "POST API and you have uploaded a {} file".format(content_type)

        # file_uploaded.save()

        return Response(response)

def index(request):
    return render(request, 'index.html')


# @csrf_exempt
class StationViewSet(viewsets.ModelViewSet):
    
    # queryset = StationInfo.objects.all()
    serializer_class = StationInfoSerializer

    def get_queryset(self):

        queryset = StationInfo.objects.all()
        stationCode=self.request.query_params.get('st_code',None)

        if stationCode is not None:
            queryset=queryset.filter(st_code=stationCode)
        
        return queryset

class observedViewSet(viewsets.ModelViewSet):

    # queryset=ObserveData.objects.all()
    print(dateInput)
    queryset=ObserveData.objects.filter(date_time=f'{dateInput}')
    # queryset=ObserveData.objects.filter(date_time='2022-11-01 06:00:00')

    # queryset=queryset.filter(date_time='2022-11-09 06:00:00')

    serializer_class=observedSerializer

class stationObservedViewSet(viewsets.ModelViewSet):
    
    queryset=StationObserved.objects.filter(forecastdate=f'{dateInput}')
    
    serializer_class=stationObservedSerializer


class figureViewSet(viewsets.ViewSet):

    def list(self, request):

        bokehPlot=returnEnacts()
        bokehJson = json.dumps(bokehPlot)
        
        return Response(bokehJson)
    


@api_view(['GET'])
def figureByParameter(request,  **kwargs):

    print(kwargs)
    category=kwargs['category']
    thisParameter=kwargs['parameter']

    if category=='emission':

        emission=returnEmissionJson(thisParameter)
        responseValue=emission

    elif category=='other':
        # thisParameter='wordFigure'
        # thisParameter=kwargs['parameter']
        jsonFig=returnPlotly()
        responseValue=jsonFig

    elif category=='district':
        thisDistrict=kwargs['parameter']
        jsonFig=returnDistrictEmission(thisDistrict)
        responseValue=jsonFig

    elif category=='district1':
        thisDistrict=kwargs['parameter']
        jsonFig=returnDistrictLanCover(thisDistrict)
        responseValue=jsonFig

    elif category=='district2':
        thisDistrict=kwargs['parameter']
        jsonFig=returnDistrictFMD(thisDistrict)
        responseValue=jsonFig

    elif category=='district3':
        thisDistrict=kwargs['parameter']
        jsonFig=returnLivestockPopulation(thisDistrict)
        responseValue=jsonFig

    
    elif category=='district4':
        thisDistrict=kwargs['parameter']
        jsonFig=returnDistrictCWD(thisDistrict)
        responseValue=jsonFig

    elif category=='correlation':
        thisParametert=kwargs['parameter']
        if thisParameter=='landcover':
            columns=returnCorrelationDF(thisParameter)
            print(columns)
        
        # jsonFig=returnDistrictCWD(thisDistrict)
        responseValue=columns


    else:
        responseValue={}
    # print(kwargs['parameter'])

    return Response(responseValue)

    if slug=='1':

        bokehPlot=returnEnacts()
        bokehJson = json.dumps(bokehPlot)
        print(bokehJson)
        responseValue=bokehJson

    elif slug=='2':
        emission=returnEmissionJson(slug)
        # print('Hello')
        # emissionJson=json.dumps(emission)
        responseValue=emission

        # worldCover=worldCoverFigure()
        # worldCoverJson = json.dumps(worldCover)
        # responseValue={1:'worldCoverJson'}

    elif slug=='3':
        
        jsonFig=returnPlotly()
        responseValue=jsonFig
        # Map=mapInitialize()
        # bdGeoRoads,nationalGeoRoads,regionalGeoRoads,zillaGeoRoads,otherGeoRoads=returnRoadGeoDataframes()


        # selectedStyle={'fillColor': '#ffff00','color': 'purple','weight': 3,'dashArray': '5, 5'}
        # Map.add_data(
        #     nationalGeoRoads,
        #     'length',add_legend=False,style_function=lambda feature:selectedStyle,
        #     layer_name="National Highway")


       
        # mymap = Map._repr_html_()

        # responseValue=json.dumps(mymap)
    elif slug=='4':

        responseValue=returnDistrictEmission()

    else:
        emission=returnEmissionJson(slug)
        # print('Hello')
        # emissionJson=json.dumps(emission)
        responseValue=emission
        # responseValue=slug


    return Response(responseValue)


# @api_view(['GET'])
def template_view(request):
    
    bdGeoRoads,nationalGeoRoads,regionalGeoRoads,zillaGeoRoads,otherGeoRoads=returnRoadGeoDataframes()

    figure = folium.Figure()
    # Map = geemap.Map(plugin_Draw = True, Draw_export = True)
    Map=geemap.Map(location=[23.8103, 90.4125],tiles='CartoDB Positron',add_google_map = False,zoom=7)
    selectedStyle={'fillColor': '#ffff00','color': 'purple','weight': 3,'dashArray': '5, 5'}
    Map.add_data(
        nationalGeoRoads,
        'length',add_legend=False,
        layer_name="National Highway")



    Map.add_to(figure)
    Map=Map._repr_html_()


    context = {
        'map': Map,
        'map_title': 'Map 1 - OpenStreetMap'
    }

    return render(request, 'map.html', context)

# def runScript(request,slug):
@api_view(['GET'])
def runScript(request):

   
    filePath=os.path.join(BASE_DIR,'observed/scripts/appName.py')
    filePath=filePath.replace('/', '//')

    out=run([sys.executable,filePath])
    
    # out=run([sys.executable,"//Volumes//dssDevelopment//djangular//APIs//observed//scripts//appName.py"])
    # out=run([sys.executable,"//Volumes//dssDevelopment//djangular//APIs//observed//scripts//appName.py",slug])

    # print(out)

    return render(request,'scripts.html')


    

