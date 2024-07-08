const fs = require('fs')
const input = fs.readFileSync('BOJ_2857.txt').toString().trim().split('\n')

const cleanedInput = input.map(line => line.trim());

let fbiAgents = [];

cleanedInput.forEach((line, index) => {
    if (line.includes('FBI')) {
        fbiAgents.push(index + 1);
    }
});

if (fbiAgents.length > 0) {
    console.log(fbiAgents.join(' '));
} else {
    console.log('HE GOT AWAY!');
}

//아 하나도 생각안난다