function solution(s, skip, index) {
  let answer = '';
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const validAlphabet = [...alphabet].filter(ch => !skip.includes(ch));
  for (let char of s) {
      const currentPos = validAlphabet.indexOf(char);
      const newPos = (currentPos + index) % validAlphabet.length;
      answer += validAlphabet[newPos];
  }

  return answer;
}

// 모르겠다 이말이야 이게 왜 답이지