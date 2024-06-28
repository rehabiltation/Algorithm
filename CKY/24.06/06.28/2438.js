const fs = require("fs");
const input = fs.readFileSync("./2438.txt").toString().trim().split();

for (let i = 1; i <= input; i++) {
  let ans = "";
  for (let j = 1; j <= i; j++) {
    ans += "*";
  }
  console.log(ans);
}
