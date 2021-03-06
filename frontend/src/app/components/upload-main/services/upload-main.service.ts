import { Injectable } from '@angular/core';
import { GenericService } from '../../../services/generic.service';

@Injectable({
  providedIn: 'root'
})
export class UploadMainService {

  constructor(private service: GenericService) { }

  public async postPDF(object: any) {
    const formData: FormData = new FormData();
    formData.append('file', object);
    const result: Object = await this.service.Post('parse/upload', formData)
      .then(response => response);
    return JSON.parse(JSON.stringify(result));
  }
}
