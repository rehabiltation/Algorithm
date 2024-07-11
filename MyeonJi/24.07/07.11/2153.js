const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

function isPrime(num) {
    if (num <= 1) return true; // 1도 소수로 간주합니다.
    if (num <= 3) return true; // 2와 3은 소수입니다.
    if (num % 2 === 0 || num % 3 === 0) return false; // 2와 3으로 나누어 떨어지면 소수가 아닙니다.
    let i = 5;
    while (i * i <= num) {
        if (num % i === 0 || num % (i + 2) === 0) return false;
        i += 6;
    }
    return true;
}

function getLetterValue(letter) {
    if (letter >= 'a' && letter <= 'z') {
        return letter.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
    } else if (letter >= 'A' && letter <= 'Z') {
        return letter.charCodeAt(0) - 'A'.charCodeAt(0) + 27;
    }
    return 0;
}

// 단어의 각 문자를 숫자로 변환하여 합계를 계산
const sum = [...input].reduce((total, letter) => total + getLetterValue(letter), 0);

// 합계가 소수인지 판별하고 결과 출력
if (isPrime(sum)) {
    console.log("It is a prime word.");
} else {
    console.log("It is not a prime word.");
}
