const fs = require('fs')
const input = fs.readFileSync('./BOJ_10872.txt').toString().split(' ')

const A = parseInt(input[0])

function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1)
  }
}

console.log(factorial(A))