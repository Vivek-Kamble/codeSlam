import { Component, OnInit } from '@angular/core';
import {UserserviceService} from '../userservice.service'

@Component({
  selector: 'app-app-sec',
  templateUrl: './app-sec.component.html',
  styleUrls: ['./app-sec.component.css']
})
export class appsecComponent {
  
  constructor(private callservice:UserserviceService){
    this.getData()
  }
  datareceived;
  getData()
  {
    this.callservice.getAll().subscribe(res=>{
      this.datareceived=res;
      console.log(this.datareceived);
    });
  }

}
