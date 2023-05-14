
import {Component} from '@angular/core';
import { SelectionModel } from '@angular/cdk/collections';

import {FlatTreeControl} from '@angular/cdk/tree';
import {MatTreeFlatDataSource, MatTreeFlattener} from '@angular/material/tree';

import { DataServiceService } from '../services/data-service.service';
import { lastValueFrom } from 'rxjs'; 

export class treeNode {
  id:number;
  select:boolean;
  item: string;
  
  children: treeNode[];
}

/** Flat node with expandable and level information */
export class treeFlatNode {
  id:number;
  select:boolean;
  item: string;

  level: number;
  expandable: boolean;
}

var TREE_DATA: treeNode[] = [

  {
    id:0,
    select:false,
    item: 'Road Layers',
    children:[
      {id:1,select:false,item: 'Primary',children:null}, 
      {id:2,select:false,item: 'Secondary',children:null}, 
      {id:3,select:false,item: 'Tertiary',children:null}
    ]
  },

  {
    id:4,
    select:false,
    item: 'Land Cover',
    children:[
      {id:5,select:false,item: 'Land use',children:null},
      {id:6,select:false,item: 'Green area',children:null},
      {id:7,select:false,item: 'Water bodies',children:null}
    ]
  },

  {
    id:8,
    select:false,
    item: 'Climate change',
    children:[
      {id:9,select:false,item: 'Number of tropical days (Max ≥ 30°C)',children:null}, 
      {id:10,select:false,item: 'Number of summer days (Max ≥ 25°C)',children:null}, 
      {id:11,select:false,item: 'Number of warm days (Max ≥ 20°C)',children:null}
    ]
  },
  

];

@Component({
  selector: 'app-nav-tree',
  templateUrl: './nav-tree.component.html',
  styleUrls: ['./nav-tree.component.css']
})

export class NavTreeComponent {

  
  observableNodeArray : any = [];

  selectedNode: any;
  onSelectedNode(node) {
    this.selectedNode = node;
  }

  constructor(
    private _dataService: DataServiceService) {

    this.treeFlattener = new MatTreeFlattener(
      this._transformer,
      this.getLevel,
      this.isExpandable,
      this.getChildren,
     );

     this.treeControl = new FlatTreeControl<treeFlatNode>(this.getLevel, this.isExpandable);
     this.dataSource = new MatTreeFlatDataSource(this.treeControl, this.treeFlattener);

     this.dataSource.data = TREE_DATA;
  }

  ngOnInit():void{
  }

  private _transformer = (node: treeNode, level: number) => {
    return {
      expandable: !!node.children && node.children.length > 0,
      id:node.id,
      select:node.select,
      item: node.item,
      level: level,
    };
  };

  /** Map from flat node to nested node. This helps us finding the nested node to be modified */
  flatNodeMap = new Map<treeFlatNode, treeNode>();

  /** Map from nested node to flattened node. This helps us to keep the same object for selection */
  nestedNodeMap = new Map<treeNode, treeFlatNode>();


  treeControl: FlatTreeControl<treeFlatNode>;
  treeFlattener: MatTreeFlattener<treeNode, treeFlatNode>;
  dataSource: MatTreeFlatDataSource<treeNode, treeFlatNode>;

    /** The selection for checklist */
    checklistSelection = new SelectionModel<treeFlatNode>(true /* multiple */);

  getLevel = (node: treeFlatNode) => node.level;
  isExpandable = (node: treeFlatNode) => node.expandable;
  getChildren = (node: treeNode): treeNode[]   => node.children;
  hasChild = (_: number, _nodeData: treeFlatNode) => _nodeData.expandable;
  hasNoContent = (_: number, _nodeData: treeFlatNode) => _nodeData.item === '';


  updateObservableNodeArray(node){
    this._dataService.setNode(node);
  }

  todoLeafItemSelectionToggle(node: treeFlatNode,$event): void {

    // console.log(node);
    const result=this.checklistSelection.select(node);
    // console.log(result);
    const nodeIndex = this.treeControl.dataNodes.indexOf(node);
    // console.log('Node Index '+ nodeIndex);

    const removeIndex = this.observableNodeArray.indexOf(node);
    // console.log('New Array Index ' + removeIndex)

    const isChecked=$event.checked;
    // console.log('In Nav Tree: Evenet Checked: ' + isChecked);


    if(isChecked){
      this.observableNodeArray.push(node);
      // console.log(node.id,node.select);
    }

    else{
      this.observableNodeArray.splice(removeIndex, 1);
    }



   this.updateObservableNodeArray(this.observableNodeArray);

    // this.dataChange(mappedArray);
    // this.dataChange(this.observableNodeArray);
   
    // console.log(this.newArray);
  }


}
