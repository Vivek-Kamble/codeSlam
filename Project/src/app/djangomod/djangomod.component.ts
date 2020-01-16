import { Component, OnInit } from '@angular/core';
import { UserserviceService } from '../userservice.service'
@Component({
  selector: 'app-djangomod',
  templateUrl: './djangomod.component.html',
  styleUrls: ['./djangomod.component.css']
})
export class DjangomodComponent{

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
