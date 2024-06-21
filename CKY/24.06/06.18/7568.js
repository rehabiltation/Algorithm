// 인풋 처리
const fs = require("fs");
const input = fs.readFileSync("./7568.txt").toString().trim().split("\n");
// 사람과 사람 정보로 구조분해할당
let [person, ...peopleInfo] = input;
// 사람 정보를 2차원 리스트 int로 변형
peopleInfo = peopleInfo.map((peoeple) =>
  peoeple.split(" ").map((num) => parseInt(num))
);
// 정답 출력할 리스트 생성
const answerList = Array();
// 사람 정보를 완전탐색을 진행하며 자기보다 큰 사람의 인원 체크
for (let i = 0; i < person; i++) {
  let count = 0;
  for (let j = 0; j < person; j++) {
    if (
      peopleInfo[i][0] < peopleInfo[j][0] &&
      peopleInfo[i][1] < peopleInfo[j][1]
    ) {
      count += 1;
    }
  }
  //   자기보다 큰 사람의 갯수 +1 한 값을 정답 리스트에 추가
  answerList.push(count + 1);
}
console.log(...answerList);
