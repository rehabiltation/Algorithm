// 인풋 받는 부분
const fs = require("fs");
const input = fs.readFileSync("./14916.txt").toString().trim();

// 5원으로 낼 수 있는 개수 체크
let fiveCount = Math.floor(input / 5);
// 2원 개수 초기값
let twoCount = 0;
// 5원으로 낼 수 있는 값을 내고 난 후 돈
let middleValue = input % 5;
// 5원으로 낼 수 있는 동전 개수가 0 이 아닐때까지
while (fiveCount > 0) {
  // 2로 나누고 나머지 값
  const checkValue = middleValue % 2;
  //   나머지 값이 없으면 반복문 탈출
  if (checkValue === 0) {
    break;
  } else {
    // 5로 낼 수 있는 거스름돈 -1 한 후 내고 난 후 돈 +5 원
    fiveCount -= 1;
    middleValue += 5;
  }
}
// 2원으로 낼 수 있는 돈 개수
twoCount += Math.floor(middleValue / 2);
// 2원으로 내고도 남았을 경우랑 남지 않을 경우 체크
if (middleValue % 2 === 0) {
  console.log(twoCount + fiveCount);
} else {
  console.log(-1);
}
