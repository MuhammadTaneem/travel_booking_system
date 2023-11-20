import {ChangeDetectionStrategy, ChangeDetectorRef, Component, Inject, OnDestroy, OnInit} from '@angular/core';
import {Subject, takeUntil} from "rxjs";
import {MatCalendar} from "@angular/material/datepicker";
import {DateAdapter, MAT_DATE_FORMATS, MatDateFormats} from "@angular/material/core";

@Component({
  selector: 'app-cuustom-date-picker-header',
  templateUrl: './custom-date-picker-header.component.html',
  styleUrls: ['./custom-date-picker-header.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CustomDatePickerHeaderComponent<D> implements OnInit, OnDestroy {
  private _destroyed = new Subject<void>();

  selectedMonth: number =0;
  selectedYear: number =0;

  months = [
    { value: 0, viewValue: 'January' },
    { value: 1, viewValue: 'February' },
    { value: 2, viewValue: 'March' },
    { value: 3, viewValue: 'April' },
    { value: 4, viewValue: 'May' },
    { value: 5, viewValue: 'June' },
    { value: 6, viewValue: 'July' },
    { value: 7, viewValue: 'August' },
    { value: 8, viewValue: 'September' },
    { value: 9, viewValue: 'October' },
    { value: 10, viewValue: 'November' },
    { value: 11, viewValue: 'December' }
  ];

  years: number[] = [];

  constructor(
    private _calendar: MatCalendar<D>,
    private _dateAdapter: DateAdapter<D>,
    @Inject(MAT_DATE_FORMATS) private _dateFormats: MatDateFormats,
    cdr: ChangeDetectorRef,
  ) {
    _calendar.stateChanges.pipe(takeUntil(this._destroyed)).subscribe(() => cdr.markForCheck());
  }

  ngOnInit(){
    this.selectedMonth = this._dateAdapter.getMonth(this._calendar.activeDate);
    this.selectedYear = this._dateAdapter.getYear(this._calendar.activeDate);
    for (let i = this.selectedYear - 15; i <= this.selectedYear + 15; i++) {
      this.years.push(i);
    }
  }


  ngOnDestroy() {
    this._destroyed.next();
    this._destroyed.complete();
  }


  onMonthChange() {
    const activeDateMonthIndex =this._dateAdapter.getMonth(this._calendar.activeDate);
    this._calendar.activeDate = this._dateAdapter.addCalendarMonths(this._calendar.activeDate, this.selectedMonth - activeDateMonthIndex)
    console.log(this._dateAdapter.getMonth(this._calendar.activeDate))
    this.onChangeYear();
  }
  onChangeYear(){
    const activeDateYear = this._dateAdapter.getYear(this._calendar.activeDate);
    this._calendar.activeDate = this._dateAdapter.addCalendarYears(this._calendar.activeDate, this.selectedYear - activeDateYear)
    console.log(this._dateAdapter.getYear(this._calendar.activeDate))
  }



  previousClicked(mode: 'month' | 'year') {
    console.log(this._calendar.activeDate)


    this._calendar.activeDate =
      mode === 'month'
        ? this._dateAdapter.addCalendarMonths(this._calendar.activeDate, -1)
        : this._dateAdapter.addCalendarYears(this._calendar.activeDate, -1);
  }

  nextClicked(mode: 'month' | 'year') {
    this._calendar.activeDate =
      mode === 'month'
        ? this._dateAdapter.addCalendarMonths(this._calendar.activeDate, 1)
        : this._dateAdapter.addCalendarYears(this._calendar.activeDate, 1);
  }
}
