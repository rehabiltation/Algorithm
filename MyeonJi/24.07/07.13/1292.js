const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(Number);

const A = input[0];
const B = input[1];

let arr = [];
let plusNum = 1;

while (arr.length < B) {
  for (let i = 0; i < plusNum; i++) {
    arr.push(plusNum)
  }
  plusNum++;
}

let sum = 0;
for (let i = A-1; i<B; i++) {
  sum += arr[i]
}

console.log(sum);