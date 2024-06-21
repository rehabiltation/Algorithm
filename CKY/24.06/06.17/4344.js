// 인풋 처리 부분
const fs = require("fs");
let [N, ...input] = fs.readFileSync("./4344.txt").toString().trim().split("\n");
// input 을 한줄씩 반복분 진행
for (line of input) {
  // 2차원 배열형태이기 때문에 한번더 Number로 치환
  let group = line.split(" ").map(Number);
  //   Number로 치환한 부분에서 사람수, 점수로 분할
  let [people, ...score] = group;
  //   초기값 선언
  const initalValue = 0;
  //   합을 구하는 reduce 함수 시행
  const total = score.reduce(
    (accmulator, currentValue) => accmulator + currentValue,
    initalValue
  );
  //   평균 구하는데 내림 처리
  const average = Math.floor(total / people);
  //   평균 넘는사람 체크
  let cnt = 0;
  //   평균 넘으면 cnt 변수 +1
  for (sco of score) {
    if (sco > average) {
      cnt += 1;
    }
  }
  //   소수점 아래 3자리까지 고정
  console.log(((cnt / people) * 100).toFixed(3) + "%");
}
