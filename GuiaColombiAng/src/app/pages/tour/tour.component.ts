import { Component, OnInit } from '@angular/core';
import { Tour } from '../../models/tour.model';
import { TourService } from 'src/app/services/tour/tour.service';

@Component({
  selector: 'app-tour',
  templateUrl: './tour.component.html',
  styleUrls: ['./tour.component.css']
})
export class TourComponent implements OnInit {

  tours: Tour[] = [];

  constructor(private tourService: TourService) { }

  ngOnInit() {
    this.getTours();
  }

  getTours(): void {
    //TODO Consume REST Service
    this.tours = this.tourService.getAllTours();
  }

}
