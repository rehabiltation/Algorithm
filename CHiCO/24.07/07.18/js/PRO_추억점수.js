function solution(name, yearning, photo) {
  let answer = []
  let score = {}
  for (let i = 0; i < name.length; i++) {
      score[name[i]] = yearning[i]
  }
  for (let i = 0; i < photo.length; i++) {
      let ans = 0;
      for (let j = 0; j < photo[i].length; j++) {
          if (score[photo[i][j]]) {
              ans += score[photo[i][j]];
          }
      }
      answer.push(ans);
  }
  return answer;
}