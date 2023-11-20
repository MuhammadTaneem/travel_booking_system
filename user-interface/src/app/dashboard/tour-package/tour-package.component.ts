import { Component } from '@angular/core';
import {
  CustomDatePickerHeaderComponent
} from "../../shaded/cuustom-date-picker-header/custom-date-picker-header.component";
@Component({
  selector: 'app-tour-package',
  templateUrl: './tour-package.component.html',
  styleUrls: ['./tour-package.component.css']
})
export class TourPackageComponent {
   tours: any[] = [
    {
      name: "Tour 1",
      description: "Description for Tour 1",
      image_1: "assets/slider/1.jpg",
      price: 100.00,
      discount: 20.00,
      location: "City A",
      duration: "3 days",
      policy: "Cancellation policy 1",
    },
    {
      name: "Tour 2",
      description: "Description for Tour 2",
      image_1: "assets/slider/2.jpg",
      price: 150.00,
      discount: 0,
      location: "City B",
      duration: "5 days",
      policy: "Cancellation policy 2",
    },
     {
       name: "Tour 3",
       description: "Description for Tour 1",
       image_1: "assets/slider/3.jpg",
       price: 100.00,
       discount: 20.00,
       location: "City C",
       duration: "3 days",
       policy: "Cancellation policy 1",
     },
    // Add more tour objects as needed
  ];
   selectedSpot!:string;
   spotList:any=[
     {
       value:"cox_bazaar",
       name:"Cox Bazaar"
     },
     {
       value:"cox_bazaar",
       name:"Bandar Ban"
     },
     {
       value:"cox_bazaar",
       name:"Khagracori"
     },
   ]
  protected readonly CustomDatePickerHeaderComponent = CustomDatePickerHeaderComponent;
}
