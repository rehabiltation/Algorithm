const fs = require('fs')
const input = fs.readFileSync('BOJ_10810.txt').toString().trim().split('\n')

const firstLine = input[0].trim().split(' ')
const N = parseInt(firstLine[0])
const M = parseInt(firstLine[1])

const arr = []
for (let i = 1; i <= M; i++) {
  const ball = input[i].trim().split(' ').map(Number)
  arr.push(ball)
}

const baskets = new Array(N).fill(0);

for (const [start, end, number] of arr) {
    for (let i = start - 1; i < end; i++) {
        baskets[i] = number;
    }
}

console.log(baskets.join(' '));