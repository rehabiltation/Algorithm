// https://school.programmers.co.kr/learn/courses/30/lessons/155652

function solution(s, skip, index) {
  // Set으로 만들어서 검색을 빠르게 함
  const skipSet = new Set(skip);

  // 알파벳 전체를 배열로 만듦
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');

  // 결과를 담을 배열
  let answer = [];

  // s의 각 문자에 대해 변환 작업을 수행
  for (let char of s) {
      let currentIndex = alphabet.indexOf(char);
      let steps = 0;

      // index만큼 이동
      while (steps < index) {
          currentIndex = (currentIndex + 1) % 26;
          if (!skipSet.has(alphabet[currentIndex])) {
              steps++;
          }
      }

      // 변환된 문자 추가
      answer.push(alphabet[currentIndex]);
  }

  // 결과 배열을 문자열로 변환해서 반환
  return answer.join('');
}
