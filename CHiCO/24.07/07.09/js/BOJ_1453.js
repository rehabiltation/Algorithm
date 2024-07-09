const fs = require('fs')
const input = fs.readFileSync('BOJ_1453.txt').toString().trim().split('\n')

const N = parseInt(input[0]); 
const seats = input[1].split(' ').map(Number); 

const MAX_COMPUTERS = 100;
let computers = new Array(MAX_COMPUTERS + 1).fill(false); 

let rejectedCount = 0;

for (let i = 0; i < N; i++) {
    let wantedSeat = seats[i];

    if (!computers[wantedSeat]) {
        computers[wantedSeat] = true;
    } else {
        rejectedCount++;
    }
}

console.log(rejectedCount);
