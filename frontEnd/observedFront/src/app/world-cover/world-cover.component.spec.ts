import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WorldCoverComponent } from './world-cover.component';

describe('WorldCoverComponent', () => {
  let component: WorldCoverComponent;
  let fixture: ComponentFixture<WorldCoverComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WorldCoverComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WorldCoverComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
