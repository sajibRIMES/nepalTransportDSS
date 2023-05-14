import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MapDataService {


  readonly APIUrl="http://127.0.0.1:8000";

  constructor(private http:HttpClient) { }

  returnNepalDistrictsGeo(){
    return this.http.get<any>('/assets/nepalGeoJSON/nepalDistricts.geojson');
  }

  returnNepalDistrictCentroid(){
    return this.http.get<any>('/assets/nepalGeoJSON/districtsCentroid.json');
  }

  returnNepalPrimaryRoad(){
    return this.http.get<any>('/assets/nepalGeoJSON/nepalRoads/roadClassified/primary.geojson');
  }

  returnNepalSecondaryRoad(){
    return this.http.get<any>('/assets/nepalGeoJSON/nepalRoads/roadClassified/secondary.geojson');
  }


  returnNepalTertiaryRoad(){
    return this.http.get<any>('/assets/nepalGeoJSON/nepalRoads/roadClassified/tertiary.geojson');
  }

  returnParameterizedProjectedValue(yearRange,parameter,scenario,model){

    let yearArray = yearRange.split(" ");
    let startYear = yearArray[0];
    let endYear = yearArray[1];

    return this.http.get<any>('/assets/CMIP6/'+parameter+'_day_'+model+'_'+scenario+'_r1i1p1f1_2015_2100.json');
  }



  returnParameterizedObservedValue(parameter){
    // tasmax_day_ACCESS-CM2_ssp585_r1i1p1f1_1950_2014.json
    return this.http.get<any>('/assets/CMIP6/'+parameter+'_day_ACCESS-CM2_ssp585_r1i1p1f1_1950_2014.json');
  }

  returnNationalRoads(){
    // return this.http.get<any>(this.APIUrl+'/transport/bd-roads?format=json')
    return this.http.get<any>('/assets/bdGeoJSON/nationalGeoRoads.geojson');
    // return this.http.get<any>('/assets/enacts/districtsTmax.geojson');
  }

  returnDistrictTmax(){
    return this.http.get<any>('/assets/enacts/districtsTmax.geojson');
  }

  returnProjectedTmax(){
    return this.http.get<any>('/assets/CMIP6/tasMaxProjection_2020_2050.geojson');
  }

  returnGeoTiff(){
    return this.http.get<any>('/assets/enacts/Daily_Tmax/1981-2021_tmax_mean.tif');
  }

  returnUpazilaGeo(){
    return this.http.get<any>('/assets/bdGeoJSON/upazila.geojson');
  }

  returnZilaGeo(){
    return this.http.get<any>('/assets/bdGeoJSON/BD_District.geojson');
  }
  
  returnDailyForecast(){
    return this.http.get<any>('/assets/bdGeoJSON/upazila_forecast_daily.json');
  }

  returnUpazilaForecastDaily(){

    return this.http.get<any>(this.APIUrl+'/forecast/daily-forecast/')
  }
  

}
