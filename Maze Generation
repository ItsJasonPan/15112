

var cols, rows;
var w=40; //40 pixel * 40 pixel each square
var grid=[];
var current;
var stack = [];

function setup() {
 createCanvas(400,400); //maze size. unit:pixel
 cols = floor(width/w); 
 rows = floor(height/w);  
 frameRate(20); //speed
 for (var j=0;j<rows;j++){  
 	for (var i=0;i<cols;i++){
 		var cell = new Cell(i,j);
 		grid.push(cell);  //create each individual cell
 	}
 }
 	current = grid[0];   //starting point (0,0)
}

function draw() {  //continously refresh draw function
  background(51);
  for(var i=0; i<grid.length;i++){
  	grid[i].show();
  } //create grids
  current.visited =true;  //mark current cell visited
  current.highlight(); //high light current cell
  //step1
  var next = current.checkNeighbors(); //check if there is unvisited neighbor
  if (next){
  	 next.visited=true; //mark the next one visited
  	//step2
  	 stack.push(current);  // put the current cell into a stack
  	//step3
  	 removeWalls(current,next); 
  	//remove the walls between current and next cell
  	//step4
  	 current = next; //new current cell
  } else if(stack.length>0){ //if no more neighbor & stack has cells
	var cell = stack.pop(); //pick the last cell we put into the stack
	current = cell; //new current cell
  }//program ends when no more no cell has unvisited cell & stack size=0
}
function index(i,j){
	if(i<0 || j<0 ||i>(cols-1) ||j>(rows-1)){
		return -1;
	}
 	return (i + j * cols);
}

function Cell(i,j){
	this.i = i;
	this.j = j;
	this.walls=[true,true,true,true];
	this.visited = false;
	this.checkNeighbors = function(){
		var neighbors = [];
		var top = grid[index(i,j-1)]
		var right = grid[index(i+1,j)]
		var bottom= grid[index(i,j+1)]
		var left = grid[index(i-1,j)]

		if (top&& !top.visited){ //check if top cell exists & unvisited
			neighbors.push(top);
		}

		if (right&& !right.visited){//check if right cell exists & unvisited
			neighbors.push(right);
		}

		if (bottom&& !bottom.visited){//check if bottom cellexists & unvisited
			neighbors.push(bottom);
		}

		if (left&& !left.visited){//check if left exists & unvisited
			neighbors.push(left);
		}
		
		if(neighbors.length>0){   //check if unvisited neighbor exist
			//randomly pick a neighbor if exsit
			var r = floor(random(0,neighbors.length));
			return neighbors[r];
		} else {
			return undefined; 
			//return undefine if there is no unvisited neighbor
		}
	} 
	this.highlight = function(){ //highlight current cell
		var x = this.i*w;
		var y = this.j*w;
		noStroke(); 
		fill(0,0,255,100);
		rect(x,y,w,w);
	}
	this.show = function(){
		var x = this.i*w;
		var y = this.j*w;
		stroke(255);
		if(this.walls[0]){
			line(x,y,x+w,y);   //up
		}

		if(this.walls[1]){
			line(x+w,y,x+w,y+w); //right
		}
 
		if(this.walls[2]){
			line(x+w,y+w,x,y+w); //bottom
		}
 
		if(this.walls[3]){
			line(x,y+w,x,y); //left
		}

		if(this.visited){
			noStroke();
			fill(255,0,255,100);
			rect(x,y,w,w);  //make the cell purple if it's visited
		}
	}
}

function removeWalls(a,b){  //remove walls bewteen current and the next cell
	var x = a.i - b.i;
	if (x === 1){  //current: right  next: left
		a.walls[3]=false;
		b.walls[1]=false;
	}
	else if (x===-1){ //current: left  next: right
		a.walls[1]=false;
		b.walls[3]=false;
	}
	var y = a.j - b.j; 
	if (y === 1){  //current: bottom  next: top
		a.walls[0]=false;
		b.walls[2]=false;
	}
	else if (y === -1){ //current: bottom  next: top
		a.walls[2]=false;
		b.walls[0]=false;
	}
}

