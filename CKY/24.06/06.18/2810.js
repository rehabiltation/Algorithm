// 인풋 받는 부분
const fs = require("fs");
const input = fs.readFileSync("./2810.txt").toString().trim().split("\n");
// 사람과 좌석 수 구조분해할당
const people = parseInt(input[0]);
const seatList = input[1].toString();
// L, S 개수 체크
const countL = seatList.match(/L/g);
const countS = seatList.match(/S/g);
// L, S 가 있는지 없는지 판단해서 길이 할당 혹은 0
const lengthL = countL ? countL.length : 0;
const lengthS = countS ? countS.length : 0;
// L(커플석) 이 없는 경우 있는경우 각각 출력 방식 변경
if (lengthL !== 0) {
  console.log(lengthL / 2 + 1 + lengthS);
} else {
  console.log(lengthS);
}
