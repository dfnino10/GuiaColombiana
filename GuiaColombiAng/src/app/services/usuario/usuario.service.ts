import { Injectable } from '@angular/core';
import { Usuario } from '../../models/usuario.model';
import { Login } from '../../models/login.model';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { URL_SERVICIOS } from '../../config/config';
import swal from 'sweetalert2'
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';


import { Router } from '@angular/router';

@Injectable()
export class UsuarioService {

  usuario: Usuario;
  menu: any[] = [];

  // Http Headers
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }

  constructor(
    public http: HttpClient,
    public router: Router,
  ) {
    this.cargarStorage();
  }

  estaLogueado() {
    return (localStorage.getItem('usuario')) ? true : false;
  }

  cargarStorage() {

    if (localStorage.getItem('usuario')) {
      this.usuario = JSON.parse(localStorage.getItem('usuario'));
      this.menu = JSON.parse(localStorage.getItem('menu'));
    } else {
      this.usuario = null;
      this.menu = [];
    }

  }

  guardarStorage(id: string, usuario: Usuario, menu?: any) {

    localStorage.setItem('id', id);
    localStorage.setItem('usuario', JSON.stringify(usuario));
    localStorage.setItem('menu', JSON.stringify(menu));

    this.usuario = usuario;
    this.menu = menu;
  }

  logout() {
    this.usuario = null;
    this.menu = [];

    localStorage.removeItem('usuario');
    localStorage.removeItem('menu');

    this.router.navigate(['/login']);
  }


  login(usuario: Login, recordar: boolean = false): Observable<any> {
    console.log('login eduard');
    if (recordar) {
      localStorage.setItem('email', usuario.username);
    } else {
      localStorage.removeItem('email');
    }

    let url = URL_SERVICIOS + '/guia/login/';
    console.log('url: ', url, 'usuario:', JSON.stringify(usuario));
    return this.http.post(url, JSON.stringify(usuario), this.httpOptions)
      .pipe(
        retry(1),
        catchError(err => {
          swal.fire('Error en el login', err.error.mensaje, 'error');
          return Observable.throw(err);
        }
        )
      )
  }


  crearUsuario(usuario: Usuario) {

    let url = URL_SERVICIOS + '/usuario';


  }

  actualizarUsuario(usuario: Usuario) {

    let url = URL_SERVICIOS + '/usuario/' + usuario._id;


  }





}
