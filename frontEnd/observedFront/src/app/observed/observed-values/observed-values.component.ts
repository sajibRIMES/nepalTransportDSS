import { Component, OnInit } from '@angular/core';
import { ObservedService } from 'src/app/services/observed.service';


@Component({
  selector: 'app-observed-values',
  templateUrl: './observed-values.component.html',
  styleUrls: ['./observed-values.component.css']
})
export class ObservedValuesComponent implements OnInit {

  constructor(private service:ObservedService) { }

  observedArray:any=[];


  ngOnInit(): void {
    this.service.observedValues().subscribe(
      data=>{
        this.observedArray=data;
      });
  }

}
