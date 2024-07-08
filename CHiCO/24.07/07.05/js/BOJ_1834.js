// const fs = require('fs')
// const input = fs.readFileSync('BOJ_1834.txt').toString().trim()

// const N = Number(input)

// let ans = 0

// for (let k = 1; k<N; k++) {
//   ans += k*(N + 1)
// }

// console.log(ans)

// 이렇게 쓰래요
const fs = require('fs');
const input = fs.readFileSync('dev/stdin').toString().trim();

const N = BigInt(input);

let sum = 0n; // 초기값을 BigInt로 설정

for (let k = 1n; k < N; k++) {
    sum += k * (N + 1n);
}

console.log(sum.toString()); // BigInt를 문자열로 변환하여 출력



// 입력이 커서 bigint라는 애를써야한다고 합니다
// bigint 를 쓸 때는 숫자 뒤에 n을 붙여서 쓰라고 합니다.