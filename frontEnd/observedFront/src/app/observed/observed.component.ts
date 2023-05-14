import { Component, OnInit } from '@angular/core';
import { ObservedService } from '../services/observed.service';

// import { MatButton } from '@angular/material';

declare var Bokeh: any;

interface selectionDropDown {
  value: string;
  viewValue: string;
}


@Component({
  selector: 'app-observed',
  templateUrl: './observed.component.html',
  styleUrls: ['./observed.component.css']
})
export class ObservedComponent implements OnInit {

  title = 'Porgressive App to View Data on Maps';
  
  opened=false;

  log(state){
    console.log(state);
    // this.service.jsonFigure().subscribe(
    //   data => {
    //     this.bokehjson = data;
    //     this.golabaljson = JSON.parse(data);
    //     Bokeh.embed.embed_item(this.golabaljson, 'bokeh-id')

    //   });
  }

  startYears: selectionDropDown[] = [
    { value: '1981', viewValue: '1981' },
    { value: '1991', viewValue: '1991' },
    { value: '2001', viewValue: '2001' },
    { value: '2011', viewValue: '2011' }
  ];

  startYear?: string;



  endYears: selectionDropDown[] = [
    { value: '1991', viewValue: '1991' },
    { value: '2001', viewValue: '2001' },
    { value: '2011', viewValue: '2011' },
    { value: '2021', viewValue: '2021' }
  ];

  endYear?: string;

  parameters: selectionDropDown[] = [
    { value: 'rr', viewValue: 'Rainfall' },
    { value: 'tamx', viewValue: 'Maximum Temperature' },
    { value: 'tmin', viewValue: 'Minimum Temperature' },
  ];

  parameter?: string;


  public bokehjson: any = [];
  golabaljson: any;
  obj: any;

 
  constructor(private service: ObservedService) { 
    // this.selectedValue='';
  }

  ngOnInit(): void { this.returnJson() }

  
  public returnJson() {


    this.service.jsonFigure().subscribe(
      data => {
        // console.log(data);
        
        this.bokehjson = data;
        this.golabaljson = JSON.parse(data);
        Bokeh.embed.embed_item(this.golabaljson, 'bokeh-id')

      });

  }



}