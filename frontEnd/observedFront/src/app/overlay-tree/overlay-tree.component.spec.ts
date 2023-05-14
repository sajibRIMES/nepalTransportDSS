import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OverlayTreeComponent } from './overlay-tree.component';

describe('OverlayTreeComponent', () => {
  let component: OverlayTreeComponent;
  let fixture: ComponentFixture<OverlayTreeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OverlayTreeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OverlayTreeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
