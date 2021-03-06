import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class GenericService {

  private api = `${environment.api}`;

  constructor(private http: HttpClient) { }

  public Get<T>(url: string): Promise<T> {
    return new Promise((resolve, reject) => {
      this.http.get<T>(this.api + url)
        .toPromise()
        .then(data => resolve(data))
        .catch(err => console.log(err));
    });
  }

  public Post<T>(url: string, data: T): Promise<T> {
    return new Promise((resolve, reject) => {
      this.http.post<T>(this.api + url, data)
        .toPromise()
        .then(result => resolve(result))
        .catch(err => console.log(err));
    });
  }
}
