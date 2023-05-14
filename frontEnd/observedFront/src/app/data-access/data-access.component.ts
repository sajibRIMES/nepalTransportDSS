import { Component, ViewChild, EventEmitter, Input, OnInit, Output, AfterViewInit } from '@angular/core';
import { NavTreeComponent } from '../nav-tree/nav-tree.component';
import { DataServiceService } from '../services/data-service.service';
import { SelectionModel } from '@angular/cdk/collections';


@Component({
  selector: 'app-data-access',
  templateUrl: './data-access.component.html',
  styleUrls: ['./data-access.component.css']
})

export class DataAccessComponent implements OnInit{

  

  
  @Input() nodeList: any = [];
  @Output() onSelected = new EventEmitter<any>();

  selectedNode: any;

  constructor(private _dataService: DataServiceService) { }

  ngOnInit():void{
    
    this._dataService.selectedNode$.subscribe((node)=>{
      this.nodeList=node;
    });
    
  }
  
  checklistSelection = new SelectionModel<any>(true /* multiple */);


  onSelectedNode(node,$event){

    node.select=!node.select;
    
    this.selectedNode=node;
    this.onSelected.emit(node);
    console.log('In Data-Access: '+ node.select);
  }
 
}
