import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styles: []
})
export class DashboardComponent implements OnInit {
  citys: any[] = [
    { value: 'steak-0', viewValue: 'Bogota' },
    { value: 'pizza-1', viewValue: 'Cúcuta' },
    { value: 'tacos-2', viewValue: 'Villavicencio' }
  ];
  categorys: any[] = [
    { value: 'steak-0', viewValue: 'Extreme' },
    { value: 'pizza-1', viewValue: 'fly' }
  ];
  constructor() { }

  ngOnInit() {
  }

}
