import { AfterViewInit, Component, OnInit,Renderer2} from '@angular/core';
import {lastValueFrom,Observable,Subscription,from } from 'rxjs';

// Service to Retrieve Data from
import { DataServiceService } from '../services/data-service.service';
import { ObservedService } from '../services/observed.service';
import { MapDataService } from '../services/map-data.service';
import { WeatherForecastService } from '../services/weather-forecast.service';


// Leaflet Declaration
import "leaflet-boundary-canvas";
import * as L from 'leaflet';
import {tileLayer } from 'leaflet';

export class geoShape{

    zillaGeo:any;
    private geoService:MapDataService
    constructor(){
        
        this.zillaGeo=this.geoService.returnZilaGeo()
        console.log(this.zillaGeo);
    }
    

    
}
