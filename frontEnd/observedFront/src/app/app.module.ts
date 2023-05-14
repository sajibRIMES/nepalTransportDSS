import { NgModule,NO_ERRORS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {HttpClientModule} from '@angular/common/http';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';

import { AgGridModule } from 'ag-grid-angular';




// import {LeafletModule} from '@asymmetrik/ngx-leaflet';


// import * as Bokeh from '@bokeh/bokehjs';
import { ObservedService } from './services/observed.service';
import { ShpaeService } from './services/shpae.service';

import { ObservedComponent } from './observed/observed.component';
import { StationsComponent } from './observed/stations/stations.component';
import { ObservedValuesComponent } from './observed/observed-values/observed-values.component';
import { StationObservedComponent } from './observed/station-observed/station-observed.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material/material.module';
import { WorldCoverComponent } from './world-cover/world-cover.component';
import { SafePipe } from './safe.pipe';
import { GeemapComponent } from './geemap/geemap.component';

// import { NestedTreeControl } from "@angular/cdk/tree";
// import { MatTreeNestedDataSource } from "@angular/material/tree";
// import { LeafletModule } from 'leaflet';
import { NgxGraphModule } from '@swimlane/ngx-graph';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { NavTreeComponent } from './nav-tree/nav-tree.component';
import { OverlayTreeComponent } from './overlay-tree/overlay-tree.component';
import { MenuComponent } from './menu/menu.component';
import { WeatherForecastComponent } from './weather-forecast/weather-forecast.component';
import { DataAccessComponent } from './data-access/data-access.component';



// import {cdkMenuTriggerFor} from 

@NgModule({

  declarations: [
    AppComponent,
    ObservedComponent,
    StationsComponent,
    ObservedValuesComponent,
    ObservedComponent,
    StationObservedComponent,
    WorldCoverComponent,
    SafePipe,
    GeemapComponent,
    NavTreeComponent,
    OverlayTreeComponent,
    MenuComponent,
    WeatherForecastComponent,
    DataAccessComponent,


  ],

  imports: [

    BrowserModule,
    BrowserAnimationsModule,
    
    FontAwesomeModule,
    
    AppRoutingModule,
    AgGridModule,
  
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    
    MaterialModule,

  ],

  providers: [
    ObservedService,
    ShpaeService
  ],
  schemas: [NO_ERRORS_SCHEMA ],

  bootstrap: [AppComponent]
})
export class AppModule { }
