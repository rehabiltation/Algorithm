const fs = require('fs');
const input = fs.readFileSync('./BOJ_25304.txt').toString().split('\n');

const totalAmount = parseInt(input[0]);


const itemCount = parseInt(input[1]);

let calculatedAmount = 0;

for (let i = 0; i < itemCount; i++) {
  const [price, count] = input[2 + i].split(' ').map(Number);
  calculatedAmount += price * count;
}

if (calculatedAmount === totalAmount) {
  console.log("Yes");
} else {
  console.log("No");
}
