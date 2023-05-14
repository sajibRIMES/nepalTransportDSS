import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

// import * as data from 'src/assets/bdGeoJSON/bdRoads.json'

@Injectable({
  providedIn: 'root'
})
export class ShpaeService {

  readonly APIUrl="http://127.0.0.1:8000";

  constructor(private http:HttpClient) { }

  getShapes(){
    // return this.http.get('/assets/bdGeoJSON/bangladesh.geojson');
    // return this.http.get('/assets/bdGeoJSON/nationalGeoRoads.geojson');
    return this.http.get<any>(this.APIUrl+'/transport/bd-roads?format=json')

  }
}
