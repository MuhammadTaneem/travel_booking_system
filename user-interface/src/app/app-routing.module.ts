import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {AppComponent} from "./app.component";
import {DashboardComponent} from "./dashboard/dashboard.component";
import {AdminModule} from "./admin/admin.module";

const routes: Routes = [
  {
    path: '',
    children: [
      {path: '', pathMatch: "full", redirectTo: 'dashboard'},
      {path: 'dashboard', component: DashboardComponent},
      { path: 'admin', loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule) },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
