// JS 노드 모듈 불러오기
let fs = require("fs");
// 파일 읽어서 string으로 변환 한 후 공백으로 분리
let input = fs.readFileSync("./1977.txt").toString().split("\n");
// 시작점 끝점 변수 선운
const start = parseInt(input[0]);
const end = parseInt(input[1]);
// 최소값 저장할 변수
let min_value = 10 ** 9;
// 1씩 증가할 변수와 총합값 저장
let number = 1;
let total = 0;
// 제곱 수가 end 보다 작을때까지 반복
while (number * number <= end) {
  // JS Math 내장함수 사용하여 제곱 진행
  if (Math.pow(number, 2) >= start && Math.pow(number, 2) <= end) {
    if (min_value >= Math.pow(number, 2)) {
      // 최소값이 10**9 로 지정해뒀기 떄문에 제일 처음 만난 최소값을 갱신
      min_value = Math.pow(number, 2);
    }
    // 범위 내의 경우 총합에 제곱 값을 더해나감
    total += Math.pow(number, 2);
  }
  //  number 라는 인덱스 1씩 증가
  number += 1;
}
// 초기값의 경우 값이 갱신되지 않았기 떄문에 -1 출력
if (total === 0) {
  console.log(-1);
} else {
  console.log(total);
  console.log(min_value);
}
