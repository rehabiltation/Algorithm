const fs = require('fs');
const input = fs.readFileSync('dev/stdin').toString().trim().split('\n');

const [N, B] = input[0].trim().split(' ');

// parseInt는 B진수의 N 값을 10진수로 돌려준다고 합니다. 
const decimal = parseInt(N, B);

console.log(decimal);
