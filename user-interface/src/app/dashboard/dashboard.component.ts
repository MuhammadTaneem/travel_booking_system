import { Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {Router} from "@angular/router";
import {
  CustomDatePickerHeaderComponent
} from "../shaded/cuustom-date-picker-header/custom-date-picker-header.component";
// @ts-ignore
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit  {

  images = [
    'assets/slider/1.jpg',
    'assets/slider/2.jpg',
    'assets/slider/3.jpg',
    'assets/slider/4.jpg',
    'assets/slider/5.jpg',
  ];

  currentImageIndex = 0;

  ngOnInit(): void {
    setInterval(() => {
      this.nextImage();
    }, 1000*5);
  }

  nextImage(): void {
    this.currentImageIndex<this.images.length-1?this.currentImageIndex +=1:this.currentImageIndex=0;
    // console.log(this.currentImageIndex);
  }

  prevImage(): void {

    this.currentImageIndex>0?this.currentImageIndex -=1:this.currentImageIndex=this.images.length-1;
    // console.log(this.currentImageIndex);
  }

  goToImage(index: number): void {
    this.currentImageIndex = index;
  }

  constructor(private router: Router) { }

  onClick() {
    this.router.navigate(['/admin']);
  }


  protected readonly CustomDatePickerHeaderComponent = CustomDatePickerHeaderComponent;
}
