import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AppSecComponent } from './app-sec.component';

describe('AppSecComponent', () => {
  let component: AppSecComponent;
  let fixture: ComponentFixture<AppSecComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AppSecComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AppSecComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
