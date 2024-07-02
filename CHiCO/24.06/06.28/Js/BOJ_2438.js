const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
const N = parseInt(input);

for (let i = 1; i <= N; i++) {
    console.log('*'.repeat(i));
}