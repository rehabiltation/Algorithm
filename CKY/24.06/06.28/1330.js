const fs = require("fs");
const input = fs.readFileSync("./1330.txt").toString().trim().split(" ");

console.log(
  parseInt(input[0]) > parseInt(input[1])
    ? ">"
    : parseInt(input[0]) === parseInt(input[1])
    ? "=="
    : "<"
);
