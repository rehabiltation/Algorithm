const fs = require('fs');
const input = fs.readFileSync('BOJ_1247.txt').toString().trim().split('\n');

let index = 0;

for (let t = 0; t < 3; t++) {
  const N = parseInt(input[index++]);
  let sum = BigInt(0);

  for (let i = 0; i < N; i++) {
    sum += BigInt(input[index++]);
  }

  if (sum === 0n) {
    console.log("0");
  } else if (sum > 0n) {
    console.log("+");
  } else {
    console.log("-");
  }
}
