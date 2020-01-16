  
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserserviceService {

  apiurl:string='http://code-slam.herokuapp.com/movies'
  constructor(private http:HttpClient) { }

  getAll()
  {
    return this.http.get(this.apiurl);
  }
  
  create(body)
  {
    return this.http.post(this.apiurl,body);
  }

  url="http://localhost:8000/api/v1/contact";
  getAll1(){
    return this.http.get(this.url);
  }
  getOne(id){
    return this.http.get(this.url);
  }
  update(id,data)
  {
    return this.http.patch(this.url+"/"+id,data);
  }
  delete(id){
    return this.http.delete(this.url+"/"+id);

  }
  add(data)
  {
    return this.http.post(this.url,data)
  }

}