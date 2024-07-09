const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const N = parseInt(input);  // 파일에서 읽어온 문자열 전체를 정수로 변환

for (let i = 1; i <= N; i++) {
    let spaces = ' '.repeat(N - i);  // 공백
    let stars = '* '.repeat(i).trim();  // 별은 공백 다음에 오기 때문에 trim() 사용
    console.log(spaces + stars);
}