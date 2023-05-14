import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ColDef } from 'ag-grid-community';
import { Observable } from 'rxjs';
import { ObservedService } from 'src/app/services/observed.service'; 

@Component({
  selector: 'app-station-observed',
  templateUrl: './station-observed.component.html',
  styleUrls: ['./station-observed.component.css']
})

export class StationObservedComponent{

  threeHourlyArray:any[]=[];
  forecastDate:any;

  columnDefs:ColDef[]=[
    {field:'stationid'},{field:'st_name'},{field:'forecastdate'},{field:'startstep'},{field:'endstep'},
    {field:'precipitation'},{field:'temperature'},{field:'relative_humidity'},{field:'dewpoint'},
    {field:'wind_speed'},{field:'visibility'},{field:'station_level_pressure'},{field:'sea_level_pressure'}
  ];

  constructor(private service:ObservedService){}
  ngOnInit(): void {

    
    this.service.threeHourlyObserved().subscribe(

      data=>{
        this.threeHourlyArray=data;
        this.forecastDate=this.threeHourlyArray[0]['forecastdate']
        // console.log(this.forecastDate)
      }
      
    );
  }

}
