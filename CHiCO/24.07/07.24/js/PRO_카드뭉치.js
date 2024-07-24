function solution(cards1, cards2, goal) {
  let i = 0, j = 0;
  
  for (let k = 0; k < goal.length; k++) {
      if (i < cards1.length && goal[k] === cards1[i]) {
          i++;
      } else if (j < cards2.length && goal[k] === cards2[j]) {
          j++;
      } else {
          return "No";
      }
  }
  
  return "Yes";
}
