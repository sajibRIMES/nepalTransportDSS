import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StationObservedComponent } from './station-observed.component';

describe('StationObservedComponent', () => {
  let component: StationObservedComponent;
  let fixture: ComponentFixture<StationObservedComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StationObservedComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StationObservedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
