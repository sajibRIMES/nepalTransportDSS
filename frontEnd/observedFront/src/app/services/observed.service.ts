import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ObservedService {

  readonly APIUrl="http://127.0.0.1:8000";
  public bokehjson : any=[];

  constructor(private http:HttpClient) { }

  returnStationList():Observable<any>{
    return this.http.get<any>(this.APIUrl + '/observed/stations/')
  }

  returnStationDetails(st_code:number){
    return this.http.get<any>(this.APIUrl+'/observed/stations/?st_code='+st_code)
    // http://127.0.0.1:8000/stations/?st_code=41923
  }


  observedValues(){
    return this.http.get<any>(this.APIUrl + '/observed/stationObserved/')
  }

  threeHourlyObserved(){
    return this.http.get<any>(this.APIUrl+'/observed/threeHourlyObserved/')
  }

  threeHourForecast(){
    return this.http.get<any>(this.APIUrl+'/forecast/hourly-forecast/')
  }


  public jsonFigure(){   
    // return this.http.get<any>(this.APIUrl + '/figures/')
    return this.http.get<any>(this.APIUrl + '/figureByParameter/1/')
  }

  public worldCover(){   
    // return this.http.get<any>(this.APIUrl + '/figures/')
    return this.http.get<any>(this.APIUrl + '/figureByParameter/2/')
  }

  public emissionFigure(){   
    // return this.http.get<any>(this.APIUrl + '/figures/')
    return this.http.get<any>(this.APIUrl + '/figureByParameter/2/')
  }

  public geemap(){
    return this.http.get<any>(this.APIUrl + '/figureByParameter/3/')
  }


  
}
