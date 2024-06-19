// 인풋처리
const fs = require("fs");
const input = fs.readFileSync("./2740.txt").toString().trim().split("\n");
// 인풋 구조분해할당
const [info, ...matrixs] = input;
// N,M 을 int로 변환
const [N, M_1] = info.split(" ").map((num) => parseInt(num));
// 첫 matrix 생성하는데 matrixs 뭉터기에서 slice 로 자른 후 map을 통해서 int로 변환
const matrixA = matrixs
  .slice(0, N)
  .map((matrix) => matrix.split(" ").map((num) => parseInt(num)));
//  두번째 matrix 정보 slice 자르며 int로 변환
const [M_2, K] = matrixs
  .slice(N, N + 1)[0]
  .split(" ")
  .map((num) => parseInt(num));
//   두번째 matrix 생성하며 slice를 통해 int로 변환
const matrixB = matrixs
  .slice(N + 1, matrixs.length)
  .map((matrix) => matrix.split(" ").map((num) => parseInt(num)));
// 행렬 곱셈 진행
for (let i = 0; i < N; i++) {
  let ans = "";
  for (let j = 0; j < K; j++) {
    let calculate = 0;
    for (let k = 0; k < M_1; k++) {
      calculate += matrixA[i][k] * matrixB[k][j];
    }
    // 곱셈 진행한 결과를 출력할 변수에 저장
    ans += calculate + " ";
  }
  //  공백제거 후 출력
  ans = ans.trim();
  console.log(ans);
}
