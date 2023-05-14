import { AfterViewInit, Component, OnDestroy, OnInit,Renderer2} from '@angular/core';
import { FormControl,FormGroup, Validators } from '@angular/forms';
import { lastValueFrom,Subscription} from 'rxjs';

// Service to Retrieve Data from
import { ObservedService } from '../services/observed.service';
import { MapDataService } from '../services/map-data.service';
import { WeatherForecastService } from '../services/weather-forecast.service';




// Leaflet Declaration
import "leaflet-boundary-canvas";
import * as L from 'leaflet';
import {tileLayer } from 'leaflet';

const mapLayers={
  dataexLayer:tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}@2x?access_token={accessToken}', {
    attribution: '',
    maxZoom: 10,
    minZoom:7,
    id: 'mapbox/outdoors-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw',
}),

layerZero:tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',{maxZoom: 30,minZoom:7}),
layerOne:tileLayer('https://api.mapbox.com/styles/v1/nazmul-rimes/ck9wljpn30kbx1is5a630hmtb/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibmF6bXVsLXJpbWVzIiwiYSI6ImNrOWFzeHNtcDA3MjAzbG50dnB0YmkxNnAifQ.usNB6Kf9PyFtKTUF1XI38g ',{maxZoom: 30,minZoom:7}),
layerTwo:tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',{maxZoom: 30,minZoom:7}),
layerThree:tileLayer('https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}',{maxZoom: 30,minZoom:7}),
layerFour:tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom: 30,minZoom:7}),
layerFive:tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png',{maxZoom: 30,minZoom:7}),
layerSix:tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',{maxZoom: 30,minZoom:7}),

};


// Bokeh Json Figure Declaration
declare var Bokeh: any;

// Location Interface for Form
interface location{value: string;viewValue: string;}
// Observed Weather Parameter Interface
interface observedParameter {value: string;viewValue: string;}
// Weather Parameter Interface for Form
interface Parameter {value: string;viewValue: string;}
// Projection Weather Parameter Inter
interface projectionParameter {value: string;viewValue: string;}

// Time Period Interface
interface Annual{value:string;viewValue:string;}
interface Month{value:string;viewValue:string;}
interface Season{value:string;viewValue:string;}

interface Model{value:string;viewValue:string;}
interface Scenario{value:string;viewValue:string;}


@Component({
  selector: 'app-geemap',
  templateUrl: './geemap.component.html',
  styleUrls: ['./geemap.component.css']

})


export class GeemapComponent implements OnInit, AfterViewInit,OnDestroy{

  // Leaflet Map Variables
  public map:any; options:any;layerControl:any;
  // Bokeh Figure Variables
  showBokeh=false; public bokehjson: any = []; golabaljson: any;
  //Tiff Required Variables
  imageLayer:any; showTiff=true;
    
    
  // Forecast Variables
  maxTemp:any; minTemp:any; maxRainfall:any;minRainfall:any;maxWind:any;minWind:any;maxHumidity:any;minHumidity:any;

  // Weather Map Variables 
  observedMap:any;forecastMap:any;projectedMap:any;

  // Tab Variables
  selectedIndex = 1;

  // Footer Component show/hide Variables
  isActiveObserved=false;isActiveForecast=true;isActiveProjected=false;

  // OverLay CDK Variables
  isOpen = false;
  // Tree Node Variables
  nodeArray:number;
  selectedNode: any;
  // Nav Tree and OverLay (Data-Access Component) Configurations
  display=false;
  layerDisplay=false;
  onPress(){this.display=!this.display; this.layerDisplay=true;}
  onLayerPress(){this.layerDisplay=!this.layerDisplay;}


  // Observed Cliamtology Varaibales
  districtObservedTmax:any;

  //  Observed Variables
  observedMax:number;
  observedMin:number;
  observedValue:number;
  observedStep:number;

  // Climate Projection Variables
  // Climate Projection Variables
  districtProjectedTmax:any;
  projectedMax:number;
  projectedMin:number;
  projectedValue:number;
  projectedStep:number;

  // Formatting slider labels


 
  // Weather Paramter Configuration Setup
  isoOpenConfigure=false;
  subscription:Subscription;

  // Nepal Variables
  maxValue:any;
  dailyMaxValues:any=[];
  nepalDailyGeoForecast:any;
  // Nepal Road Layer Variables
  nepalPrimaryRoadLayer:any;
  nepalSecondaryRoadLayer:any;
  nepalTertiaryRoadLayer:any;
  
  // Constructor Callong Services
  constructor(
    private _weather_forecast_service:WeatherForecastService,
    private mapDataService:MapDataService,
    private observedService: ObservedService){
    }
  
  // On Initial
  ngOnInit(){
    // this.nepalDailyForecastMap();
     this.returnAllLocations();
     this.forecastMap=this.onSelectionChangeGenerateWeatherMap(this.selectedWeatherParameter)
  }

  // Constructing Distric and District Centroid Dictionary
  async returnAllLocations(){
    let centroidData=this.mapDataService.returnNepalDistrictCentroid();
    centroidData.subscribe((data)=>{
      for(let key in data){
        this.locations.push({'value':String(data[key]['district_id']),'viewValue':data[key]['District']});
        this.locationXY.push({'value':String(data[key]['district_id']),'viewValue':data[key]['centroid']});
      }
    });
    
  }

// Setting up fly to location
async onLocationChange(ob){
  for(let key in this.locationXY){
    let valueIndex=this.locationXY[key]['value']

    if (ob.value=='0'){this.map.flyTo([28.3949, 84.1240], 7);  }
    else if (ob.value===valueIndex){this.map.flyTo(this.locationXY[key]['viewValue'], 10); }
  }
}

  //  Configuring Forecast  Forms

    // Location Selection
    selectedLocation: string = '0'
    locations:location[]=[{'value': '0', 'viewValue': 'Nepal'}];
    locationXY:any=[];

    // Weather Parameter Selection 
    selectedWeatherParameter: string = "tmax";
    parameters: Parameter[] = [
      {value: 'tmax', viewValue: 'Maximum Temperature'},
      {value: 'tmin', viewValue: 'Minimum Temperature'},
      {value: 'precip', viewValue: 'Precipitation'},
      {value: 'rh', viewValue: 'Relative Humidity'},
      {value: 'ws', viewValue: 'Wind Speed'},
    ];
  
    // Form and Form Control
    locationControl = new FormControl(this.locations[0].value,Validators.required);
    parameterControl = new FormControl(this.parameters[0].value,Validators.required);

    // Forecast Form Group
    form = new FormGroup({
      location:this.locationControl,
      parameter: this.parameterControl,

    });

  // Observed Form Elements
    // Observed Weather Parameter Selections
    selectedObservedWeatherParameter: string = "tas";
    observedWeatherParameters: observedParameter[] = [
      {value: 'tas', viewValue: 'Mean-Temperature'},
      {value: 'tasmax', viewValue: 'Maximum-Temperature'},
      {value: 'tasmin', viewValue: 'Minimum-Temperature'},
      {value: 'pr', viewValue: 'Precipitation'},
    ];
  
  // Observed Form and Form Control
  observedWeatherParameterControl = new FormControl(this.observedWeatherParameters[0].value,Validators.required);

  // Observed Form Group
  observedForm = new FormGroup({
    location:this.locationControl,
    observedParameters: this.observedWeatherParameterControl

  });


  // Projection Form Elements
  // Projection Weather Paramter Selection
  selectedProjectionWeatherParameter: string = "tas";
  projectionWeatherParameters: projectionParameter[] = [
    {value: 'tas', viewValue: 'Mean-Temperature'},
    {value: 'tasmax', viewValue: 'Maximum-Temperature'},
    {value: 'tasmin', viewValue: 'Minimum-Temperature'},
    {value: 'pr', viewValue: 'Precipitation'},
  ];
  
  // Time-Period Selection
  selectedTimePeriod:string='ann'
  annual:Annual[]=[{value:'ann',viewValue:'Annual'}]

  months:Month[]=[
    {value: 'jan', viewValue: 'January'},{value: 'feb', viewValue: 'February'},
    {value: 'mar', viewValue: 'March'},{value: 'apr', viewValue: 'April'},
    {value: 'may', viewValue: 'May'},{value: 'jun', viewValue: 'June'},
    {value: 'jul', viewValue: 'July'},{value: 'aug', viewValue: 'August'},
    {value: 'sep', viewValue: 'September'},{value: 'oct', viewValue: 'October'},
    {value: 'nov', viewValue: 'November'},{value: 'dec', viewValue: 'December'}
  ]

  seasons:Season[]=[
    {value: 'djf', viewValue: 'December-January-February'},
    {value: 'mam', viewValue: 'March-April-May'},
    {value: 'jja', viewValue: 'June-July-August'},
    {value: 'son', viewValue: 'September-October-November'},
  ]

  // Scenario Selection
  selectedScenario:string='ssp585'
  scenarios:Scenario[]=[
    {value: 'ssp245', viewValue: 'SSP2-4.5'},
    {value: 'ssp585', viewValue: 'SSP5-8.5'},
  ];

  // Model Selection
  selectedModel:string='ACCESS-CM2'
  models:Model[]=[
    {value: 'ACCESS-CM2', viewValue: 'ACCESS-CM2'},
    {value: 'IITM-ESM', viewValue: 'IITM-ESM'},
    {value: 'NorESM2-MM', viewValue: 'NorESM2-MM'},
    {value: 'TaiESM1', viewValue: 'TaiESM1'},
    {value: 'NESM3', viewValue: 'NESM3'},
    {value: 'MRI-ESM2-0', viewValue: 'MRI-ESM2-0'},
    {value: 'MPI-ESM1-2-HR', viewValue: 'MPI-ESM1-2-HR'},
    {value: 'BCC-CSM2-MR', viewValue: 'BCC-CSM2-MR'},
    {value: 'MIROC6', viewValue: 'MIROC6'},
    {value: 'CanESM5', viewValue: 'CanESM5'},
  ];


  // Projection Form Control
  projectionParameterControl = new FormControl(this.projectionWeatherParameters[0].value,Validators.required);
  annualControl = new FormControl(this.annual[0].value,Validators.required);
  monthControl = new FormControl(this.months[0].value,Validators.required);
  seasonControl= new FormControl(this.seasons[0].value,Validators.required);
  scenarioControl=new FormControl(this.scenarios[0].value,Validators.required);
  modelControl=new FormControl(this.models[0].value,Validators.required);

// Projection Form Group
  projectionForm = new FormGroup({
    location:this.locationControl,
    projectionParameter: this.projectionParameterControl,
    time:this.annualControl,
    model:this.modelControl,
    scenario: this.scenarioControl

  });


  formatObservedLabel= (value: number) => {

    let parameterSymbol:string;

    var myLocalVariable = this.selectedObservedWeatherParameter;

    if (myLocalVariable === 'pr'){parameterSymbol='mm'}
    else {parameterSymbol='°C'}

    return `${value}`+`\u00A0` +`${parameterSymbol}` 

  }

  formatForecastLabel= (value: number) => {

    let parameterSymbol:string;

    var myLocalVariable = this.selectedProjectionWeatherParameter;
    
    if (myLocalVariable === 'pr'){parameterSymbol='mm'}
    else {parameterSymbol='°C'}

    return `${value}`+`\u00A0` +`${parameterSymbol}` 

  }



// Generating Observed Map
// Setting Up Observed Bottom Slider
  // Observed Slider Value
observedSliderValue:any; observedSliderYearValue:any=1;
// Observed slider Format Label
obSliderValue:any; obSliderMin:1; obSliderMax:6; obSliderStep:1

observedSliderMap = new Map([
  ['1', '1950 1959'], ['2', '1960 1969'],['3', '1970 1979'],['4', '1980 1989'],['5', '1990 1999'],['6', '2000 2014'],
  ]);

formatObservedSliderLabel(value: number): string {
  if (value === 1) { return "1950 1959";}
  else if (value === 2) { return '1960 1969';}
  else if (value === 3) { return '1970 1979';}
  else if (value === 4) { return '1980 1989';}
  else if (value === 5) { return '1990 1999';}
  else if (value === 6) { return '2000 2014';}
  else return "1950 1959";
}

// Generating Observed map on Parameter Selection 
onSelectionChangObservedWeatherMap(ob){

  console.log('Weather Parameter on Selection Change: ' +this.selectedObservedWeatherParameter);

  if (this.selectedObservedWeatherParameter === 'pr'){

    // this.formatLabel(){}

    console.log(this.selectedObservedWeatherParameter)
  }
  this.onObservedSlideChange(this.observedValue,this.selectedObservedWeatherParameter,this.observedSliderYearValue);
}
// Initiating Observed on Slider Change
onObservedSlideChange(observedValue,selectedObservedWeatherParameter,observedSliderYearValue){

  this.observedLayer(observedValue,selectedObservedWeatherParameter,observedSliderYearValue);
}
// Retrieving Observed Value from Map-Data Service
async returnObservedValues(observedValue,selectedObservedWeatherParameter,observedSliderYearValue){

  let retrievingParameter$=this.mapDataService.returnParameterizedObservedValue(selectedObservedWeatherParameter);
  let parameterValue=await lastValueFrom(retrievingParameter$);
  let yearValues=this.observedSliderMap.get(`${observedSliderYearValue}`)
  console.log('Map Retrieved: ' + yearValues);
  let yearArray = yearValues.split(" ");
  let startYear = yearArray[0];
  let endYear = yearArray[1];

  var arrayObject= Object.values(parameterValue['year_'+startYear+'_'+endYear]);
  const max=Math.max.apply(null,arrayObject);
  const min=Math.min.apply(null,arrayObject);

  this.observedMax=Math.round(max);
  this.observedMin=Math.round(min);

  let scale=(this.observedMax-this.observedMin)/(this.observedMax-this.observedMin);
  this.observedStep=scale;

  return arrayObject;
}

// Constructing Observed Map Layer
async observedLayer(observedValue,selectedObservedWeatherParameter,observedSliderYearValue){

  if(this.projectedMap){this.projectedMap.clearLayers();}
  if(this.forecastMap){this.forecastMap.clearLayers();}
  if(this.observedMap){this.observedMap.clearLayers();}

  let arrayObject=await this.returnObservedValues(observedValue,selectedObservedWeatherParameter,observedSliderYearValue);

  let geo$ = this.mapDataService.returnNepalDistrictsGeo();
  let geoData = await lastValueFrom(geo$); 

  for(let i=0;i<77;i++){
    geoData['features'][i]['properties'][selectedObservedWeatherParameter]=arrayObject[i];
  }


  this.observedValue=observedValue;
  let roundedMaxValue = 0;

  if ( String(this.observedValue) == 'undefined'){
    roundedMaxValue =Math.round(this.observedMax);
    console.log('Rounded Max Value When Second Slider Value is Undefined:  '+roundedMaxValue);
  }

  if ( String(this.observedValue) != 'undefined'){
    roundedMaxValue =Math.round(this.observedValue);
    console.log('Second Slider Selected Value:  '+roundedMaxValue);
  }

  let roundedMinValue = Math.round(this.projectedMin);
  if (selectedObservedWeatherParameter!='tasmin'){

    function styleFunction(feature){
    
      if (Math.round(feature.properties[selectedObservedWeatherParameter])>= roundedMaxValue) {return {"color": "purple","weight": 1,"opacity": 0.65};}
      else if (Math.round(feature.properties[selectedObservedWeatherParameter]) <= roundedMaxValue) {return {"color": "blue","weight": 1,"opacity": 0.65};}
      else return {"color": "green","weight": 1,"opacity": 0.65};
    }

    this.observedMap=L.geoJSON(geoData,{style: styleFunction});
  }

  else if (selectedObservedWeatherParameter=='tasmin'){

    function styleFunction(feature){
    
      if (Math.round(feature.properties[selectedObservedWeatherParameter])<= roundedMinValue) {return {"color": "purple","weight": 1,"opacity": 0.65};}
      else if (Math.round(feature.properties[selectedObservedWeatherParameter]) >= roundedMinValue) {return {"color": "blue","weight": 1,"opacity": 0.65};}
      else return {"color": "green","weight": 1,"opacity": 0.65};
    }

    this.observedMap=L.geoJSON(geoData,{style: styleFunction});
  }
  

  var toolTipParameter='';

  if (selectedObservedWeatherParameter==='tasmax'){toolTipParameter='Maximum Temperature: ';}
  else if (selectedObservedWeatherParameter==='tasmin'){toolTipParameter='Minimum Temperature: ';}
  else if (selectedObservedWeatherParameter==='tas'){toolTipParameter='Average Temperature: ';}
  else if (selectedObservedWeatherParameter==='pr'){toolTipParameter='Average Rainfall: ';}


  this.observedMap.bindTooltip(
    function (layer) { 
      return 'District: ' 
      + layer.feature.properties.District  
      + "<br>" + toolTipParameter 
      + String(Math.round(layer.feature.properties[selectedObservedWeatherParameter]))
      
    });

  this.observedMap.addTo(this.map);
}



// ------------- Generation Forcast Map From Here -------------

// Generating Forecast map on Parameter Selection 
  onSelectionChangeGenerateWeatherMap(ob){
    if(this.forecastMap){this.forecastMap.clearLayers();}
    this.forecastMap=this.nepalDailyForecastMap(this.selectedWeatherParameter);
  }

  // Return Nepal Boundaries
  async returnNepalDistrictsGeometry(){
    let geo$ = this.mapDataService.returnNepalDistrictsGeo();
    let geoData = await lastValueFrom(geo$); 

    return geoData;
  }

 // Return nepal Daily Forecast 
  async nepalDailyDistrictForecast(){
    
    let geoData=await this.returnNepalDistrictsGeometry();

    let dailyForecast$=this._weather_forecast_service.returnNepalDistrictForecastDaily();
    let districtForeastDaily=await lastValueFrom(dailyForecast$);

    var maxTemp=Math.max(...districtForeastDaily.map(value=>value.tmax));
    var minTemp=Math.min(...districtForeastDaily.map(value=>value.tmin));
    var maxRain=Math.max(...districtForeastDaily.map(value=>value.precip));
    var maxRh=Math.max(...districtForeastDaily.map(value=>value.rh));
    var maxWs=Math.max(...districtForeastDaily.map(value=>value.ws));


    this.dailyMaxValues.push(maxTemp);
    this.dailyMaxValues.push(minTemp);
    this.dailyMaxValues.push(maxRain);
    this.dailyMaxValues.push(maxRh);
    this.dailyMaxValues.push(maxWs);


    for(let i=0;i<districtForeastDaily.length;i++){

      geoData['features'][i]['properties']['tmax']=districtForeastDaily[i].tmax
      geoData['features'][i]['properties']['tmin']=districtForeastDaily[i].tmin
      geoData['features'][i]['properties']['precip']=districtForeastDaily[i].precip
      geoData['features'][i]['properties']['rh']=districtForeastDaily[i].rh
      geoData['features'][i]['properties']['ws']=districtForeastDaily[i].ws
   
    }

    return this.dailyMaxValues,geoData;
  }

// Map Styling based on parameter and max value
mapStyleByParameter(geoData,maxValue,parameter){

  if (parameter==='tmin'){

    function styleFunction(feature){
      let roundedMaxValue =Math.round(maxValue);
      if (Math.round(feature.properties[parameter])<= roundedMaxValue) {return {"color": "purple","weight": 1,"opacity": 0.65};}
      else if (Math.round(feature.properties[parameter]) >= roundedMaxValue) {return {"color": "blue","weight": 1,"opacity": 0.65};}
      else return {"color": "green","weight": 1,"opacity": 0.65};
    }

    this.forecastMap=L.geoJSON(geoData,{style: styleFunction});

  }

  else{

    function styleFunction(feature){
      let roundedMaxValue =Math.round(maxValue);
      if (Math.round(feature.properties[parameter]) >= roundedMaxValue) {return {"color": "purple","weight": 1,"opacity": 0.65};}
      else if (Math.round(feature.properties[parameter]) <= roundedMaxValue) {return {"color": "blue","weight": 1,"opacity": 0.65};}
      else return {"color": "green","weight": 1,"opacity": 0.65};
    }

    this.forecastMap=L.geoJSON(geoData,{style: styleFunction});
  }

   
  var toolTipParameter='';

  if (parameter==='tmax'){toolTipParameter='Maximum Temperature: ';}
  else if (parameter==='tmin'){toolTipParameter='Minimum Temperature: ';}
  else if (parameter==='precip'){toolTipParameter='Maximum Rainfall: ';}
  else if (parameter==='rh'){toolTipParameter='Maximum Humidity: ';}
  else if (parameter==='ws'){toolTipParameter='Maximum Windspeed: ';}

  this.forecastMap.bindTooltip(
    function (layer) { 
      return 'District: ' 
      + layer.feature.properties.District  
      + "<br>" + toolTipParameter 
      + String(Math.round(layer.feature.properties[parameter]))
      
    });
  
  return this.forecastMap;
}

// Finally Generating Nepal District Wise forecast Map
async nepalDailyForecastMap(selectedWeatherParameter){

  
  this.selectedWeatherParameter=selectedWeatherParameter;
  console.log('Inside Forecast Map: ' +selectedWeatherParameter);

  let geoData:any;
  this.dailyMaxValues,geoData=await this.nepalDailyDistrictForecast();
  

  if (this.selectedWeatherParameter === 'tmax'){
    let maxValue=this.dailyMaxValues[0];
    this.forecastMap= this.mapStyleByParameter(geoData,maxValue,this.selectedWeatherParameter)
  }

  else if (this.selectedWeatherParameter === 'tmin'){
    let maxValue=this.dailyMaxValues[1];
    this.forecastMap= this.mapStyleByParameter(geoData,maxValue,this.selectedWeatherParameter)
  }

  else if (this.selectedWeatherParameter === 'precip'){
    let maxValue=this.dailyMaxValues[2];
    this.forecastMap= this.mapStyleByParameter(geoData,maxValue,this.selectedWeatherParameter)
  }


  else if (this.selectedWeatherParameter === 'rh'){
    let maxValue=this.dailyMaxValues[3];
    this.forecastMap= this.mapStyleByParameter(geoData,maxValue,this.selectedWeatherParameter)
  }


  else if (this.selectedWeatherParameter === 'ws'){
    let maxValue=this.dailyMaxValues[4];
    this.forecastMap= this.mapStyleByParameter(geoData,maxValue,this.selectedWeatherParameter)
  }


  this.forecastMap.addTo(this.map);

  return this.forecastMap;

}

// ------------ Configuring Projection Layer With Slider From Here ------------
  // slider Format Label
  sliderMap = new Map([
    ['1', '2021 2050'],['2','2031 2060'],['3','2041 2070'],['4','2051 2080'],['5','2061 2090'],['6','2071 2100'],
    ]);

  // Projected Slider Value
  projectedSliderValue:any; projectedSliderYearValue:any=1; yearSliderValue:any=1;

// Formating Year Slider label
formatProjectedSliderLabel(value: number): string {

  if (value === 1) { return '2021 2050';}
  else if (value === 2) { return '2031 2060';}
  else if (value === 3) { return '2041 2070';}

  else if (value === 4) { return '2051 2080';}
  else if (value === 5) { return '2061 2090';}
  else if (value === 6) { return '2071 2100';}

  else return "2021 2050";
}




// Projection Map Generate On Selection Change
onSelectionChangeGenerateProjectionMap(ob){
  this.onYearChange(
    this.projectedMax,this.yearSliderValue,this.selectedTimePeriod,this.selectedProjectionWeatherParameter,
    this.selectedScenario,this.selectedModel
  );
}


onYearChange(projectedValue,yearValues,timeperiod,parameter,scenario,model){
  
  console.log('Selected Projection Weather Parameter: '+parameter);

  if(this.observedMap){this.observedMap.clearLayers();}
  if(this.forecastMap){this.forecastMap.clearLayers();}
  if(this.projectedMap){this.projectedMap.clearLayers();}


  this.projectionLayer(projectedValue,yearValues,timeperiod,parameter,scenario,model)
}

// Get Projection Data Based Slected Parameter and Year Slider
async returnProjectedValue(projectedValue,yearValues,timeperiod,parameter,scenario,model){

  this.projectedSliderYearValue=this.sliderMap.get(`${yearValues}`); 

  // Retrieve Data From Service
  let retrievingParameter$=this.mapDataService.returnParameterizedProjectedValue(
    this.projectedSliderYearValue,
    parameter,
    scenario,
    model
    );

  let parameterValue=await lastValueFrom(retrievingParameter$);

  // console.log(parameterValue);

  let yearArray = this.projectedSliderYearValue.split(" ");
  let startYear = yearArray[0];
  let endYear = yearArray[1];

  var arrayObject= Object.values(parameterValue['year_'+startYear+'_'+endYear]);
  // console.log(arrayObject);

  const max=Math.max.apply(null,arrayObject);
  const min=Math.min.apply(null,arrayObject);

  // this.projectedMax=Math.round(max);
  this.projectedMax=Math.round(max);
  this.projectedMin=Math.round(min);
  // this.projectedValue=this.projectedMin;

  let scale=(this.projectedMax-this.projectedMin)/(this.projectedMax-this.projectedMin);
  this.projectedStep=scale;

  return arrayObject;
}

// Generate Projection Layer
async projectionLayer(projectedValue,yearValues,timeperiod,parameter,scenario,model){

  if(this.projectedMap){this.projectedMap.clearLayers();}
  if(this.forecastMap){this.forecastMap.clearLayers();}

  let arrayObject=await this.returnProjectedValue(projectedValue,yearValues,timeperiod,parameter,scenario,model);


  let geo$ = this.mapDataService.returnNepalDistrictsGeo();
  let geoData = await lastValueFrom(geo$); 

  for(let i=0;i<77;i++){
    geoData['features'][i]['properties'][parameter]=arrayObject[i];
  }

  this.projectedValue=projectedValue;

  let roundedMaxValue = 0;

  if ( String(this.projectedValue) == 'undefined'){
    roundedMaxValue =Math.round(this.projectedMax);
    console.log('Rounded Max Value When Second Slider Value is Undefined:  '+roundedMaxValue);
  }

  if ( String(this.projectedValue) != 'undefined'){
    roundedMaxValue =Math.round(this.projectedValue);
    console.log('Second Slider Selected Value:  '+roundedMaxValue);
  }


  let roundedMinValue = Math.round(this.projectedMin);
  if (parameter!='tasmin'){

    function styleFunction(feature){
      if (Math.round(feature.properties[parameter])>= roundedMaxValue) {return {"color": "purple","weight": 1,"opacity": 0.65};}
      else if (Math.round(feature.properties[parameter]) <= roundedMaxValue) {return {"color": "blue","weight": 1,"opacity": 0.65};}
      else return {"color": "green","weight": 1,"opacity": 0.65};
    }
    this.projectedMap=L.geoJSON(geoData,{style: styleFunction});
  }

  else if (parameter=='tasmin'){
    function styleFunction(feature){
      if (Math.round(feature.properties[parameter])<= roundedMinValue) {return {"color": "purple","weight": 1,"opacity": 0.65};}
      else if (Math.round(feature.properties[parameter]) >= roundedMinValue) {return {"color": "blue","weight": 1,"opacity": 0.65};}
      else return {"color": "green","weight": 1,"opacity": 0.65};
    }
    this.projectedMap=L.geoJSON(geoData,{style: styleFunction});
  }
  

  var toolTipParameter='';

  if (parameter==='tasmax'){toolTipParameter='Maximum Temperature: ';}
  else if (parameter==='tasmin'){toolTipParameter='Minimum Temperature: ';}
  else if (parameter==='tas'){toolTipParameter='Average Temperature: ';}
  else if (parameter==='pr'){toolTipParameter='Average Rainfall: ';}


  this.projectedMap.bindTooltip(
    function (layer) { 
      return 'District: ' 
      + layer.feature.properties.District  
      + "<br>" + toolTipParameter 
      + String(Math.round(layer.feature.properties[parameter]))
      
    });

  this.projectedMap.addTo(this.map);
}

// Map Data Selection for Added Over Layer (Road Layers at This Moment)
onSelectedNode(node){
  this.selectedNode=node;
  // console.log(this.selectedNode.id+':'+this.selectedNode.select);
  if ((this.selectedNode.id==1) && (this.selectedNode.select==true)){ this.nepalPrimaryRoadLayer=this.addNepalPrimaryRoad();}
  else if((this.selectedNode.id==1) && (this.selectedNode.select==false)){this.nepalPrimaryRoadLayer.clearLayers();}

  if ((this.selectedNode.id==2) && (this.selectedNode.select==true)){ this.nepalSecondaryRoadLayer=this.addNepalSecondaryRoad();}
  else if((this.selectedNode.id==2) && (this.selectedNode.select==false)){this.nepalSecondaryRoadLayer.clearLayers();}
  
  if ((this.selectedNode.id==3) && (this.selectedNode.select==true)){ this.nepalTertiaryRoadLayer=this.addNepalTertiaryRoad();}
  else if((this.selectedNode.id==3) && (this.selectedNode.select==false)){this.nepalTertiaryRoadLayer.clearLayers();}
}

  // Show Configure Box
  showConfiguration(isoOpenConfigure){this.isoOpenConfigure = !this.isoOpenConfigure;}
  // Toggle Bokeh Figure Overlay
  showBokehFigure(isOpen,showBokeh){
    // this.isoOpenConfigure = !this.isoOpenConfigure;
    this.isOpen = !this.isOpen;
    this.showBokeh=true;
    this.returnJson();
  }

  

  // Trigger Tab Clicked Function 
  tabClicked(selectedIndex){
    
    this.selectedIndex=selectedIndex;
    console.log('Tab Clicked: ' + this.selectedIndex);
    if (this.selectedIndex==0){

      this.isActiveObserved=true;
      this.isActiveForecast=false;
      this.isActiveProjected=false;

      if(this.observedMap){this.observedMap.clearLayers();}
      else if(this.forecastMap){this.forecastMap.clearLayers();}
      else if(this.projectedMap){this.projectedMap.clearLayers();}
  
      this.observedMap=this.observedLayer(this.observedValue,this.selectedObservedWeatherParameter,this.observedSliderYearValue);
    }
    
    else if (this.selectedIndex==1){

      this.isActiveObserved=false;
      this.isActiveForecast=true;
      this.isActiveProjected=false;

      if(this.observedMap){this.observedMap.clearLayers();}
      else if(this.forecastMap){this.forecastMap.clearLayers();}
      else if(this.projectedMap){this.projectedMap.clearLayers();}

      this.forecastMap=this.onSelectionChangeGenerateWeatherMap(this.selectedWeatherParameter);

    }

    else if (this.selectedIndex==2){

      this.isActiveObserved=false;
      this.isActiveForecast=false;
      this.isActiveProjected=true;
      
      if(this.observedMap){this.observedMap.clearLayers();}
      else if(this.projectedMap){this.projectedMap.clearLayers();}
      else if(this.forecastMap){this.forecastMap.clearLayers();}

      this.projectionLayer(this.projectedValue,this.yearSliderValue,'ann','tasmax','ssp585','ACCESS-CM2')

    }

    return this.selectedIndex
  }

    
 
  // Initializing Map with Options
  initMap(){
    this.options=this.getOptions();
    this.map=L.map('map',this.options)
  }
  
  // Return Initial Option for the Map
  getOptions() {
    this.options = {
      layers: [mapLayers.layerZero],
      center:[28.3949, 84.1240],
      
      // center:[23.8103,89.915800],
      // center:[23.721814, 88.504932],
      zoom:7,
      // zoomSnap: 0.25,
      zoomControl: false,
      fullscreenControl: true,
      fullscreenControlOptions: {
      position: 'topleft'
  }
    };

    return this.options;
  }

    // Layer Control for the Map
    layerControls() {
    
      var baseLayers= {
      "Dataex Layer":mapLayers.dataexLayer,
      "Base Layer":mapLayers.layerZero,
      "Gray Scale": mapLayers.layerOne,
      "Bangla Labels": mapLayers.layerTwo,
      "Topography": mapLayers.layerThree,
      "Terrain":mapLayers.layerFive,
      "Aerial":mapLayers.layerSix,
      "Open Street": mapLayers.layerFour
    }
    this.layerControl = L.control.layers(baseLayers).addTo(this.map);
  
    return this.layerControl;
    }


// Adding Road Overlay Data : Primary Road
async addNepalPrimaryRoad(){

  let primaryRoadResponse=this.mapDataService.returnNepalPrimaryRoad();
  let primaryRoads=await lastValueFrom(primaryRoadResponse);

  // console.log(primaryRoads);

  var layerStyle = {"color": "red","weight": 5,"opacity": 0.65};

  this.nepalPrimaryRoadLayer = L.geoJSON(primaryRoads,{
      style: layerStyle,
      onEachFeature: function (f, l) {
        l.bindTooltip('<pre>'+JSON.stringify(f.properties,null,' ').replace(/[\{\}"]/g,'')+'</pre>');
      },
  })

  this.nepalPrimaryRoadLayer.addTo(this.map);

  return this.nepalPrimaryRoadLayer;
}

// Adding Road Overlay Data : Secondary Road
async addNepalSecondaryRoad(){

  let secondaryRoadResponse=this.mapDataService.returnNepalSecondaryRoad();
  let secondaryRoads=await lastValueFrom(secondaryRoadResponse);

  // console.log(secondaryRoads);

  var layerStyle = {"color": "blue","weight": 5,"opacity": 0.65};

  this.nepalSecondaryRoadLayer = L.geoJSON(secondaryRoads,{
      style: layerStyle,
      onEachFeature: function (f, l) {
        l.bindTooltip('<pre>'+JSON.stringify(f.properties,null,' ').replace(/[\{\}"]/g,'')+'</pre>');
      },
      
  })

  this.nepalSecondaryRoadLayer.addTo(this.map);

  return this.nepalSecondaryRoadLayer;
}

// Adding Road Overlay Data : Tertiary Road
async addNepalTertiaryRoad(){

  let tertiaryRoadResponse=this.mapDataService.returnNepalTertiaryRoad();
  let tertiaryRoads=await lastValueFrom(tertiaryRoadResponse);

  console.log(tertiaryRoads);

  var layerStyle = {"color": "yellow","weight": 5,"opacity": 0.65};

  this.nepalTertiaryRoadLayer = L.geoJSON(tertiaryRoads,{
      style: layerStyle,
      onEachFeature: function (f, l) {
        l.bindTooltip('<pre>'+JSON.stringify(f.properties,null,' ').replace(/[\{\}"]/g,'')+'</pre>');
      },
      
  })

  this.nepalTertiaryRoadLayer.addTo(this.map);

  return this.nepalTertiaryRoadLayer;
}


// Return Bokeh Div JshonFigure from Service
public returnJson() {

  this.observedService.jsonFigure().subscribe(
    data => {
      // console.log(data);
      this.bokehjson = data;
      this.golabaljson = JSON.parse(data);
      Bokeh.embed.embed_item(this.golabaljson, 'bokeh-id');

    });

    return this.bokehjson;

}
    
// Adding Map and Data in AfterView
ngAfterViewInit(): void {
  this.initMap();
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}