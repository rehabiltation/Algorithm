const fs = require("fs");
const input = fs.readFileSync("./1551.txt").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map((num) => parseInt(num));
const listA = input[1].split(",").map((num) => parseInt(num));

console.log(listA, N, K);
