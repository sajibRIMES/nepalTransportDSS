import { NgModule } from '@angular/core';


import { MatButtonModule} from '@angular/material/button';
import {MatButtonToggleModule} from '@angular/material/button-toggle';
import {MatIconModule} from '@angular/material/icon';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatMenuModule} from '@angular/material/menu';

import {MatSidenavModule} from '@angular/material/sidenav';
import {MatSlideToggleModule} from '@angular/material/slide-toggle';
import {MatInputModule} from '@angular/material/input';


import {MatFormFieldModule} from '@angular/material/form-field';
import {MatSelectModule} from '@angular/material/select';

import {MatTreeModule} from '@angular/material/tree';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatCardModule} from '@angular/material/card';
import {MatDividerModule} from '@angular/material/divider';
import {MatTooltipModule} from '@angular/material/tooltip';
import {MatBadgeModule} from '@angular/material/badge';
import {MatExpansionModule} from '@angular/material/expansion';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatListModule} from '@angular/material/list';
import {OverlayModule } from '@angular/cdk/overlay';
import {MatSliderModule} from '@angular/material/slider';
import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatTabsModule} from '@angular/material/tabs';
import {DragDropModule} from '@angular/cdk/drag-drop';
import {MatStepperModule} from '@angular/material/stepper';
import {MatBottomSheetModule} from '@angular/material/bottom-sheet';
// import {OverlayModule} from '@angular/cdk/overlay';

const MaterialComponents = [
  MatSlideToggleModule,
  MatButtonModule,
  MatButtonToggleModule,
  MatIconModule,

  MatInputModule,
  MatFormFieldModule,
  MatSelectModule,
  MatMenuModule,
  MatSidenavModule,
  MatToolbarModule,
  MatTreeModule,
  MatCheckboxModule,
  MatCardModule,
  MatDividerModule,
  MatTooltipModule,
  MatBadgeModule,
  MatExpansionModule,
  MatGridListModule,
  MatListModule,
  OverlayModule,
  MatSliderModule,
  MatDatepickerModule,
  MatTabsModule,
  DragDropModule,
  MatStepperModule,
  MatBottomSheetModule

]

@NgModule({

  imports: [MaterialComponents],
  exports: [MaterialComponents]

})
export class MaterialModule { }
