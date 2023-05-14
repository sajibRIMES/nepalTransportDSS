import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

export class TodoItemNode {
  children: TodoItemNode[];
  item: string;
}

@Injectable({
  providedIn: 'root'
})
export class DataServiceService {

  node$=new BehaviorSubject<any>([]);
  // node$=new BehaviorSubject<TodoItemNode[]>([]);
  selectedNode$=this.node$.asObservable();


  constructor() { }


  setNode(node:any){
    this.node$.next(node);

  }

  showContent(){
    return this.node$.getValue()
  }


}
