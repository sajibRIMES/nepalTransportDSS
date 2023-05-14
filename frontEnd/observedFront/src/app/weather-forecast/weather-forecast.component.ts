import { Component, OnInit,AfterViewInit,ViewChild} from '@angular/core';
import {MatAccordion} from '@angular/material/expansion'
import { DataAccessComponent } from '../data-access/data-access.component';

import { WeatherForecastService } from '../services/weather-forecast.service';
import { MapDataService } from '../services/map-data.service';
import { lastValueFrom,Subscription } from 'rxjs';

@Component({
  selector: 'app-weather-forecast',
  templateUrl: './weather-forecast.component.html',
  styleUrls: ['./weather-forecast.component.css']
})


export class WeatherForecastComponent implements OnInit{

  @ViewChild(MatAccordion) accordion: MatAccordion;

  maxTemp:any;
  minTemp:any;
  maxRainfall:any;
  minRainfall:any;
  maxWind:any;
  minWind:any;
  maxHumidity:any;
  minHumidity:any;


  dailyMaxMin  = [];

  subscription:Subscription;

  constructor(
    private _weather_forecast_service:WeatherForecastService,
    private dataService:MapDataService){}

  ngOnInit(){
    

    this.nepalMaxMin();
    // this.loadDailyMaxMin();
  }

  async nepalMaxMin(){


    let maxMin$=this._weather_forecast_service.returnNepalDailyMaxMin();
    this.dailyMaxMin=await lastValueFrom(maxMin$);

    // console.log(dailyMaxMin[0][0]);


    this.maxRainfall=this.dailyMaxMin[0][0];
    this.minRainfall=this.dailyMaxMin[0][1];

    this.maxTemp=this.dailyMaxMin[1][0];
    this.minTemp=this.dailyMaxMin[1][1];

    this.maxHumidity=this.dailyMaxMin[3][0];
    this.minHumidity=this.dailyMaxMin[3][1];

    this.maxWind=this.dailyMaxMin[4][0];
    this.minWind=this.dailyMaxMin[4][1];




    this._weather_forecast_service.changeValue(this.maxTemp);



  }

  loadDailyMaxMin(){
    this._weather_forecast_service.getDailyMaxMin().subscribe(

      response=>{
        this.dailyMaxMin=response;

        this.maxTemp=response['Temperature']['maximum'];
        this.minTemp=response['Temperature']['minimum'];

        this.maxRainfall=response['Rainfall']['maximum'];
        this.minRainfall=response['Rainfall']['minimum'];

        this.maxWind=response['Wind Speed']['maximum'];
        this.minWind=response['Wind Speed']['minimum'];

        this.maxHumidity=response['Relative Humidity']['maximum'];
        this.minHumidity=response['Relative Humidity']['minimum'];


        this._weather_forecast_service.changeValue(this.maxTemp);
       

        // console.log(response);
      }

    );
  }

}
