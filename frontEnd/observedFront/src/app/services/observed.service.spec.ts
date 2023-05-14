import { TestBed } from '@angular/core/testing';

import { ObservedService } from './observed.service';

describe('ObservedService', () => {
  let service: ObservedService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ObservedService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
