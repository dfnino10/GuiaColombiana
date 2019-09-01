import { Injectable } from '@angular/core';
import { Tour } from "../../models/tour.model";
import { HttpClient } from '@angular/common/http';
import { TOURS } from "./tourMock";

@Injectable({
  providedIn: 'root'
})
export class TourService {

  tours: Tour[] = [];

  constructor(private httpService: HttpClient) { }

  getAllTours(): Tour[] {
    this.tours = TOURS;
    return this.tours;
  }

  /*register(username: String, password: String, first_name: String, last_name: String, email: String): Observable<any> {  
    this.messageService.add('RegisterService: Login call');
    var obj = { username: username, password: password, first_name: first_name, last_name: last_name, email: email }
    return of(this.httpClient.post(this.API_URL + '/gallery/addUser', JSON.stringify(obj), httpOptions).subscribe((data:  Response) => {
       if(data[0].fields.username==username) {
           this.router.navigate(['/gallery']);
           this.messageService.add('Usuario adicionado');
       } else {
        this.messageService.add('Usuario o contraseña incorrectos');
       }
      }));
  } */


}
