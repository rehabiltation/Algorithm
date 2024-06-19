// input 받는 부분
const fs = require("fs");
// 공백제거 후 개행으로 split
const input = fs.readFileSync("./1551.txt").toString().trim().split("\n");
// N, K 값을 구조분해할당 처리하며 int로 변환
const [N, K] = input[0].split(" ").map((num) => parseInt(num));
// A라는 List도 , 를 기준으로 분할하여 int로 변환
let listA = input[1].split(",").map((num) => parseInt(num));
// 반복 횟수 체크
let count = 0;
// 반복문이 K 번 진행
while (count < K) {
  // listA 길이 체크
  const listLength = listA.length;
  //   반복문 진행하며 임시 저장공간 생성
  const checkList = Array();
  //   계산 값을 임시 공간에 저장
  for (let i = 0; i < listLength - 1; i++) {
    checkList.push(listA[i + 1] - listA[i]);
  }
  //   끝난 후 임시저장한 리스트 listA에 덮어 씌우고 반복 횟수 증가
  listA = checkList;
  count += 1;
}
const result = listA.join(",");
console.log(result);
