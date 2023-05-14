import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ObservedValuesComponent } from './observed-values.component';

describe('ObservedValuesComponent', () => {
  let component: ObservedValuesComponent;
  let fixture: ComponentFixture<ObservedValuesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ObservedValuesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ObservedValuesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
