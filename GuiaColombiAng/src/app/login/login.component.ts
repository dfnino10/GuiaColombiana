import { Component, OnInit } from '@angular/core';
import { Usuario } from '../models/Usuario.model';
import { Login } from '../models/login.model';
import { NgForm } from '@angular/forms';
import { UsuarioService } from '../services/service.index';
import { Router } from '@angular/router';
import Swal from 'sweetalert2'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(public router: Router, public _usuarioService: UsuarioService) { }

  ngOnInit() {
  }
  email: string = "";
  password: string = "";
  recuerdame: any;

  hola() {
    console.log("hello");
  }
  submitted = false;


  onSubmit() {
    console.log("que esta");
    // this.submitted = true;
  }
  ingresar(forma: NgForm) {
    console.log(forma);
    if (forma.invalid) {
      Swal.fire('Oops...', 'revisa los datos ingresados', 'error')
      return;
    }

    let userLogin = new Login(forma.value.email, forma.value.password);

    this._usuarioService.login(userLogin, forma.value.recuerdame)
      .subscribe(data => {
        this.goDashboard(data)
      });
  }

  goDashboard(data) {
    if (data.message.split(" ")[0] === "Bienvenido")
      this.router.navigate(['/dashboard']);
    else
      Swal.fire('Oops...', 'Correo o Contraseña incorrecta!', 'error')

  }
}
