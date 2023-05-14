import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GeemapComponent } from './geemap.component';

describe('GeemapComponent', () => {
  let component: GeemapComponent;
  let fixture: ComponentFixture<GeemapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GeemapComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GeemapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
