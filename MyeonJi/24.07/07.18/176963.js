// https://school.programmers.co.kr/learn/courses/30/lessons/176963

function solution(name, yearning, photo) {
  // 이름과 그리움 점수를 매핑하는 딕셔너리 생성
  const yearningMap = {};
  for (
    let i = 0; 
    i < name.length; 
    i++
    ) {
    yearningMap[name[i]] = yearning[i];
  }

  // 각 사진의 추억 점수를 계산할 결과 배열
  const result = [];

  // 각 사진을 순회하며 추억 점수를 계산
  for (let arr of photo) {
      let score = 0;
      for (let a of arr) {
          if (yearningMap[a]) {
              score += yearningMap[a];
          }
      }
      result.push(score);
  }

  return result;
}