import { Component } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})

export class MenuComponent {

  display=true;

  onPress(){
    this.display=!this.display;

  }

  c0 = "primary";
  c1 = "primary";
  c2 = "primary";
  c3 = "primary";
  c4 = "primary";
  

}
