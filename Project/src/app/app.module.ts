import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { appsecComponent } from './app-sec/app-sec.component';
import {HttpClientModule,HttpClient} from '@angular/common/http';
import { HomeComponent } from './home/home.component';
import { ContactComponent } from './contact/contact.component'
import { FormsModule } from '@angular/forms'
import {RouterModule} from '@angular/router';
import { UserserviceService } from './userservice.service';

import { DjangomodComponent } from './djangomod/djangomod.component';
import { NotfoundComponent } from './notfound/notfound.component'

@NgModule({
  declarations: [
    AppComponent,
    appsecComponent,
    HomeComponent,
    ContactComponent,
    DjangomodComponent,
    NotfoundComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot([
      {path:"home",component:HomeComponent},
      {path:"contact",component:ContactComponent},
      {path:"django",component:DjangomodComponent},
      {path:"data",component:appsecComponent},
      // {path:"product/addproduct",component:AddProductComponent},
      // {path:"product/:id",component:ViewProductComponent},
      {path:"**",component:NotfoundComponent},
    ]),
    // HttpModule
  ],
  providers: [UserserviceService,HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }
