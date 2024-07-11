// 큰일남 하나도 모르겠음

const fs = require("fs");

// 입력을 받기
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 알파벳 빈도를 저장할 객체 생성
const frequency = {};

// 각 줄의 각 문자를 순회하면서 빈도 계산
input.forEach(line => {
    for (const char of line) {
        if (char >= 'a' && char <= 'z') {
            if (!frequency[char]) {
                frequency[char] = 0;
            }
            frequency[char]++;
        }
    }
});

// 가장 높은 빈도 찾기
let maxFrequency = 0;
for (const char in frequency) {
    if (frequency[char] > maxFrequency) {
        maxFrequency = frequency[char];
    }
}

// 가장 높은 빈도를 가진 알파벳을 알파벳 순으로 정렬하여 결과 출력
const result = [];
for (const char in frequency) {
    if (frequency[char] === maxFrequency) {
        result.push(char);
    }
}

console.log(result.sort().join(''));
