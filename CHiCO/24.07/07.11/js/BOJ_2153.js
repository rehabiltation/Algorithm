const fs =  requrie('fs')
const input = fs.readFileSync('BOJ_2153.txt').toString().trim().split('\n')

function getWordValue(word) {
  let value = 0;
  for (let char of word) {
      if (char >= 'a' && char <= 'z') {
          value += char.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
      } else if (char >= 'A' && char <= 'Z') {
          value += char.charCodeAt(0) - 'A'.charCodeAt(0) + 27;
      }
  }
  return value;
}

function isPrime(num) {
  if (num <= 1) return true; 
  if (num === 2) return true;
  if (num % 2 === 0) return false;
  for (let i = 3; i * i <= num; i += 2) {
      if (num % i === 0) return false;
  }
  return true;
}

const word = input;
const wordValue = getWordValue(word);

if (isPrime(wordValue)) {
  console.log('It is a prime word.');
} else {
  console.log('It is not a prime word.');
}
