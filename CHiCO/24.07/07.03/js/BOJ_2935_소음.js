const fs = require('fs')
const input = fs.readFileSync('BOJ_2935.txt').toString().split('\n')

const A = BigInt(input[0])
const Y = input[1].trim()
const B = BigInt(input[2])


if (Y === '+') {
  console.log((A + B).toString())
}
else {
  console.log((A * B).toString())
}
// 개 븅신같은 문제