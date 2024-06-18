// 인풋 불러오는 부분
let fs = require("fs");
// trim 으로 공백 제거 후 " "으로 쪼개기
let input = fs.readFileSync("./2163.txt").toString().trim().split(" ");
// N, M 값을 input 으로 받아오기
N = parseInt(input[0]);
M = parseInt(input[1]);
// 1, 1 인 경우 쪼갤 필요가 없어서 바로 0 출력
if (N === 1 && M === 1) {
  console.log(0);
} else {
  console.log(N * M - 1);
}
