const readline = require("readline")
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

let input;

rl.on('line', function(line) {
  input = line;
  rl.close();
}).on('close', function() {
  solution(parseInt(input))
  process.exit;
}) 

function solution(number) {
  for (let i = 1; i <= number; i++) {
    console.log('*'.repeat(i))
  } 
}