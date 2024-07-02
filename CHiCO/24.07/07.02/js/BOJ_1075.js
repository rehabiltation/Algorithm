const fs = require('fs')
const input = fs.readFileSync('BOJ_1075.txt').toString().split('\n')

const N = parseInt(input[0]);
const F = parseInt(input[1]);

const base = Math.floor(N / 100) * 100;
let result = 100;

for (let i = 0; i < 100; i++) {
  const candidate = base + i;
  if (candidate % F === 0) {
    result = i;
    break;
  }
}

console.log(result.toString().padStart(2, '0'));