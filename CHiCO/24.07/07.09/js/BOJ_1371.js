const fs = require('fs');
const input = fs.readFileSync('BOJ_1371.txt').toString().trim().split('\n');

const text = input.join('');
const counts = new Array(26).fill(0);

for (let char of text) {
    if (char >= 'a' && char <= 'z') {
        counts[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }
}

let maxCount = 0;
for (let count of counts) {
    if (count > maxCount) {
        maxCount = count;
    }
}

let result = '';
for (let i = 0; i < 26; i++) {
    if (counts[i] === maxCount) {
        result += String.fromCharCode('a'.charCodeAt(0) + i);
    }
}

console.log(result);
