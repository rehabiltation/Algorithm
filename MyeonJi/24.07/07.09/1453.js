const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]); // 손님의 수
const requests = input[1].split(' ').map(Number); // 손님이 원하는 자리 번호

const seats = new Array(100).fill(false); // 1번부터 100번까지 자리, false는 비어있음을 의미
let rejectedCount = 0; // 거절당한 손님의 수

requests.forEach(seat => {
    if (seats[seat - 1]) {
        // 자리가 이미 사용 중이면 거절
        rejectedCount++;
    } else {
        // 자리가 비어있으면 사용 중으로 표시
        seats[seat - 1] = true;
    }
});

console.log(rejectedCount);
