import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  selectedFile: File = null;

  percentage: number = 0;
  result: string = null;

  constructor(private _httpClient: HttpClient) {

  }

  onFileSelected(event) {
    this.selectedFile = event.target.files[0];
    console.log(this.selectedFile);
  }

  onUpload() {
    if (this.selectedFile) {
      var fd = new FormData();
      fd.append('rawFile', this.selectedFile);
      this._httpClient.post('http://localhost:3000/upload', fd).subscribe(res => {
        console.log(res);
        this.percentage = parseFloat(res.toString()) * 100;
        if (this.percentage > 75) {
          this.result = 'Hight';
        } else if (this.percentage > 50) {
          this.result = 'Medium';
        } else if (this.percentage > 25) {
          this.result = 'Low';
        } else {
          this.result = 'Very Low';
        }
      })
    }else{
      this.selectedFile = null;
      this.percentage = 0;
      this.result = null;
    }
  }

  // naivebayes(){
  //   this._httpClient.get('http://localhost:3000/naivebayes').subscribe(res => {
  //     console.log(res);
  //   })
  // }

}
