const fs = require('fs')
const input = fs.readFileSync('./BOJ_1330.txt').toString().split(' ')


const A = parseInt(input[0])
const B = parseInt(input[1])

if (A > B) {
  console.log('>')
} else if (A < B) {
  console.log('<')
} else {
  console.log('==')
}