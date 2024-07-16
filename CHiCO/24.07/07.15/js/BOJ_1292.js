const fs = require('fs')
const input = fs.readFileSync('BOJ_1292.txt').toString().trim().split(' ')

const A = Number(input[0])
const B = Number(input[1])

let arr = []

for (let i = 1; arr.length < B; i++){
  for (let j = 0; j < i; j++){
    arr.push(i)
  }
}

let ans = 0
for (let k = A - 1; k < B; k++){
  ans += arr[k]
}

console.log(ans)