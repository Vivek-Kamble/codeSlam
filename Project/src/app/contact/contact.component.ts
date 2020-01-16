import { Component, OnInit } from '@angular/core';
// import { Http } from '@angular/http';
import { UserserviceService } from '../userservice.service';


@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {

  constructor(private product:UserserviceService) { }
  
  messageStatusHidden=false;

  ngOnInit() {
  }

  addProduct(f)
  {
    this.product.add(f.value).subscribe(res=>{
      res;
      console.log(f);
      this.messageStatusHidden=true;
      console.log(this.messageStatusHidden);      
      f.reset();
    });
  } 

}
