const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(Number);

const A = input[0];
const B = input[1];

// A와 B의 순서를 정리
const min = Math.min(A, B);
const max = Math.max(A, B);

// 등차수열 합 공식 사용
const n = max - min + 1;
const sum = (n * (min + max)) / 2;

console.log(sum);
