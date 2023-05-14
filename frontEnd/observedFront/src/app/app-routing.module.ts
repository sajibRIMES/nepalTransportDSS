import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ObservedComponent } from './observed/observed.component';
import { StationsComponent } from './observed/stations/stations.component';
import { ObservedValuesComponent } from './observed/observed-values/observed-values.component';
import { StationObservedComponent } from './observed/station-observed/station-observed.component';

import { WorldCoverComponent } from './world-cover/world-cover.component';
import { AppComponent } from './app.component';
import { GeemapComponent } from './geemap/geemap.component';

import { NavTreeComponent } from './nav-tree/nav-tree.component';
import { OverlayTreeComponent } from './overlay-tree/overlay-tree.component';
import { WeatherForecastComponent } from './weather-forecast/weather-forecast.component';
import { DataAccessComponent } from './data-access/data-access.component';






const routes: Routes = [
  { path: '', component: GeemapComponent },
  { path: 'observedClimatology', component: ObservedComponent },
  // {path:'',component:AppComponent},
  { path: 'stations', component: StationsComponent },
  { path: 'observed', component: ObservedValuesComponent },
  { path: 'stationObserved', component: StationObservedComponent },

  { path: 'worldCover', component: WorldCoverComponent },
  { path:'nav',component:NavTreeComponent},

  { path:'weather',component:WeatherForecastComponent},

  { path:'send',component:NavTreeComponent},
  { path:'receive',component:DataAccessComponent}



];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
