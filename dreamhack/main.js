const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n'); //  /workspaces/algorithm-PS/dreamhack/exam.txt or /dev/stdin
const [n,...arr] = input;
let copy = arr.slice()
copy.sort() 
if(copy.toString()===arr.toString() ){
    console.log('INCREASING');
}
else if(copy.reverse().toString()===arr.toString()){
    console.log('DECREASING');
}
else{
    console.log('NEITHER');
}
