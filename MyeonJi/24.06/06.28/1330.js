const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input;
let list = [];
rl.on('line', function(line) {
  input = line;
  rl.close();
}).on("close", function() {
  list = input.split(' ').map((el) => parseInt(el)); 
  solution(list);
  process.exit();
});

function solution(input){
  const [a, b] = input;
  
  if (a < b) {
    console.log("<")
  }
  else if (a > b) {
    console.log(">")
  }
  else {
    console.log("==")
  }
}
