import { Component, OnInit } from '@angular/core';
import { ObservedService } from '../services/observed.service';

declare var Bokeh: any;

@Component({
  selector: 'app-world-cover',
  templateUrl: './world-cover.component.html',
  styleUrls: ['./world-cover.component.css']
})

export class WorldCoverComponent implements OnInit {

  public bokehjson: any = [];
  golabaljson: any;
  obj: any;

  constructor(private service: ObservedService) { }

  ngOnInit(): void {this.returnJson()}

  public returnJson() {


    this.service.worldCover().subscribe(
      data => {
        this.bokehjson = data;
        this.golabaljson = JSON.parse(data);
        Bokeh.embed.embed_item(this.golabaljson, 'bokeh-id')

      });

  }


}
