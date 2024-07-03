let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();
let N = parseInt(input);
let ans = '';

for (let i = 1; i <= N; i++) {
  ans += ' '.repeat(N - i) + '* '.repeat(i).trim() + '\n';
}

console.log(ans);
