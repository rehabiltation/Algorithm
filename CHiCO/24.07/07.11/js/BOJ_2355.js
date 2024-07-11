const fs =  require('fs')
const input = fs.readFileSync('BOJ_2355.txt').toString().trim().split(' ')

const A = parseInt(input[0]);
const B = parseInt(input[1]);

let sum = 0;
let start = Math.min(A, B);
let end = Math.max(A, B);

for (let i = start; i <= end; i++) {
    sum += i;
}

console.log(sum);

// 시간초과 어케 안나게함?