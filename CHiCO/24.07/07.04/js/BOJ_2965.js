const fs =  require('fs')
const input = fs.readFileSync('BOJ_2965.txt').toString().trim().split(' ')

const [A, B, C] = input

const X = B - A
const Y = C - B

let ans = X>Y ? X-1 : Y-1

console.log(ans)

// 이건 왜 되는것이지