// chronal caliberation
const { readFile } = require('node:fs');

(() => {
	readFile('./input.txt', (err, data) => {
		if (err) { 
			console.error(err);
			return;
		}

		const str = data.toString().split("\n");
		let output = 0;
		for (let i = 0; i < str.length; i++) {
			output += Number(str[i]);
		}

		console.log(output)
	})
})();