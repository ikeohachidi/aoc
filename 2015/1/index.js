const { readFile } = require('fs');

const solution = () => {
    readFile('./input.txt', (err, data) => {
        if (err) { 
            console.error(err);
            return;
        }

        const d = data.toString().split('');
        let total = 0; 
        d.forEach((b, idx) => {
            if (b === '(') {
                total++;
            } else {
                total--;
            }

            if (total === -1) {
                console.log(idx + 1);
            }
        });

        console.log(total)
    })
}
solution();