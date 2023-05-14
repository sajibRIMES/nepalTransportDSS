import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})


export class WeatherForecastService {

  readonly APIUrl="http://127.0.0.1:8000";

  constructor(private http:HttpClient) {
    // this.loadDailyMaxMin();
   }

  private valueSource$=new BehaviorSubject(20);
  currentValue$=this.valueSource$.asObservable();

  getDailyMaxMin() {
    return this.http.get<any>(this.APIUrl+'/forecast/daily-max-min');
  }

  changeValue(value: number) {
    this.valueSource$.next(value);
  }

  showContent(){
    return this.valueSource$.getValue()
  }

  returnUpazilaForecastDaily(){

    return this.http.get<any>(this.APIUrl+'/forecast/daily-forecast/')
  }

  returnNepalDistrictForecastDaily(){
    return this.http.get<any>(this.APIUrl+'/forecast/forecast-from-url/districts/daily/')
  }

  returnNepalDailyMaxMin(){
    return this.http.get<any>(this.APIUrl+'/forecast/day-max-min/daily/max-min/');
  }
  // 

}
