// 인풋 처리 부분
const fs = require("fs");
const input = fs.readFileSync("./9506.txt").toString().trim().split("\n");
// of 를 통해서 input 값 순회
for (num of input) {
  // String 으로 되어있는 부분 int 로 치환하여 -1 인 경우 반복문 탈출 (사실 필요없음 한번에 읽기 때문에)
  if (parseInt(num) === -1) {
    break;
  } else {
    // value 로 num 이라는 변수 Int 변환
    const value = parseInt(num);
    // 리스트 생성
    let numList = Array();
    //  반복문을 value 재곱근 까지 진행
    for (let i = 1; i <= Math.sqrt(value); i++) {
      //  value 값이 나눠 떨어질 경우
      if (value % i === 0) {
        // 공약수기 떄문에 리스트에 추가
        numList.push(i);
        // 1로 나눈 경우 제외하고 리스트 추가
        if (num / i !== value) {
          numList.push(num / i);
        }
      }
    }
    // 숫자가 큰 순서대로 정렬
    numList.sort((a, b) => {
      return a - b;
    });
    // reduce 초기값 선언
    const init = 0;
    // reduce 통해서 총합 구하기
    const total = numList.reduce((acc, current) => acc + current, init);
    // 공약수들 총합이 원래 수와 같은경우
    if (total === value) {
      //  값들 문자열로 변환하여 + 기호 붙여서 변수에 저장
      let ans = value + " = ";
      for (i in numList) {
        // 마지막 경우 "+" 기호 제외
        if (parseInt(i) !== numList.length - 1) {
          ans += numList[i] + " + ";
        } else {
          ans += numList[i];
        }
      }
      //   ans 변수 출력
      console.log(ans);
      //   외의 경우 아래 문구 출력
    } else {
      console.log(`${value} is NOT perfect.`);
    }
  }
}
