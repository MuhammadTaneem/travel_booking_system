import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {DashboardComponent} from "../dashboard/dashboard.component";
import {AdminDashboardComponent} from "./admin-dashboard/admin-dashboard.component";

const routes: Routes = [
  {
    path: '',
    // component: AppComponent,
    children: [
      {path: '', pathMatch: "full", redirectTo: 'dashboard'},
      {path: 'dashboard', component: AdminDashboardComponent},
      // {path: 'admin', component: AdminModule},
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminRoutingModule { }
