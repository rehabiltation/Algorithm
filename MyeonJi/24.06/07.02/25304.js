const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];
rl.on('line', function(line) {
  input.push(line);
}).on('close', function() {
  const X = parseInt(input[0]);
  const N = parseInt(input[1]);
  let calculatedTotal = 0;

  for (let i = 2; i < 2 + N; i++) {
    const [a, b] = input[i].split(' ').map(Number);
    calculatedTotal += a * b;
  }

  if (calculatedTotal === X) {
    console.log("Yes");
  } else {
    console.log("No");
  }
  process.exit();
});
