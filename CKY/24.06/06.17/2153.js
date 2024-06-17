// 에라토스테네스의 체
function primeCheck(checkNumber) {
  // 이 문제에서는 1도 소수라 판단해서 0만 소수 예외 처리한 후 나머지 false 로 초기화
  let primeList = Array(1).fill(true).concat(Array(10000).fill(false));
  // 최대 52 * 20 개 까지 공간이 필요하지만 넉넉하게 10000 선언
  for (let i = 2; i <= Math.sqrt(10000); i++) {
    // false 인 경우 i 수는 소수이기 때문에 그 제곱수부터 i 를 더해나간 수를 true 처리
    if (primeList[i] === false) {
      for (let j = i * i; j <= 10000; j += i) {
        primeList[j] = true;
      }
    }
  }
  // 들어온 값의 true, false 판단으로 소수인지 체크
  return primeList[checkNumber];
}
// 인풋 받아오는 부분
const fs = require("fs");
// vscode 에서는 txt 로 처리 => 백준은 /dev/stdin 으로 변형 // trim 으로 공백제거
const input = fs.readFileSync("./2153.txt").toString().trim().split("");
// 총합 변수
let total = 0;
// input 에서 word 한개씩 반복문 진행
for (word of input) {
  // 대문자인지 판단
  if (word === word.toUpperCase()) {
    // 대문자의 경우 -38 을 하여서 27 부터 시작
    total += word.charCodeAt() - 38;
  } else {
    // 소문자의 경우 -96 을 하여서 1 부터 시작
    total += word.charCodeAt() - 96;
  }
}
// 소수판단하여 소수의 경우 아닌 경우 출력 형식 변경
if (primeCheck(total)) {
  console.log("It is not a prime word.");
} else {
  console.log("It is a prime word.");
}
