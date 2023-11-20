// material.module.ts
import { NgModule } from '@angular/core';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatIconModule} from '@angular/material/icon';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatNativeDateModule} from '@angular/material/core';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import {MatSelectModule} from '@angular/material/select';
@NgModule({
  exports: [
    MatInputModule,
    MatButtonModule,
    MatDatepickerModule,
    MatIconModule,
    MatFormFieldModule,
    MatNativeDateModule,
    MatSlideToggleModule,
    MatSelectModule

  ],
})
export class MaterialModule {}
