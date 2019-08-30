
import { NgModule } from '@angular/core';
import { PAGES_ROUTES } from './pages.routes';

import { SharedModule } from '../shared/shared.module';

import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

import { PagesComponent } from './pages.component';

import { DashboardComponent } from './dashboard/dashboard.component';


import { AccoutSettingsComponent } from './accout-settings/accout-settings.component';
import { ProfileComponent } from './profile/profile.component';
import { UsuariosComponent } from './usuarios/usuarios.component';
import { BusquedaComponent } from './busqueda/busqueda.component';

@NgModule({
    declarations: [
        ProfileComponent,
        PagesComponent,
        DashboardComponent,
        AccoutSettingsComponent,
        UsuariosComponent,
        BusquedaComponent
    ],
    exports: [
        DashboardComponent,

    ],
    imports: [
        CommonModule,
        SharedModule,
        PAGES_ROUTES,
        FormsModule,
    ]
})
export class PagesModule { }
