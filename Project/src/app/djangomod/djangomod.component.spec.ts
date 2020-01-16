import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DjangomodComponent } from './djangomod.component';

describe('DjangomodComponent', () => {
  let component: DjangomodComponent;
  let fixture: ComponentFixture<DjangomodComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DjangomodComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DjangomodComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
