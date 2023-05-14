import { Component, OnInit } from '@angular/core';
import { ObservedService } from 'src/app/services/observed.service';

@Component({
  selector: 'app-stations',
  templateUrl: './stations.component.html',
  styleUrls: ['./stations.component.css']
})


export class StationsComponent implements OnInit {


  stationArray:any;
  selectedStation?:any;
  stationDetails?:any;

  a_value?:any;
  
  constructor(private service:ObservedService) { 
    this.returnStationList();
  
  }

  // stationArray?:[{'st_code':'0000','st_name':'None','lat':'None','lon':'None'}];

  ngOnInit(): void {
    this.returnStationList();

  }

  returnStationList(){
    this.service.returnStationList().subscribe(

      data=>{
        this.stationArray=data;
      });
  }

  stationClicked = (station:number) => {

    this.service.returnStationDetails(station).subscribe(
      data=>{
        this.stationDetails=data;
        console.log(data);
      }
    );

    // );
    // console.log(station.st_code);
  }

}
