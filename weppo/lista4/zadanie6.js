const fs = require('fs');
const readline = require('readline');


(async () => {
	const
	rl = readline.createInterface({ input: fs.createReadStream('logs.txt') }),
	occurances = {}

	for await (let line of rl) {
		line = line.split(" ")
		usr = String(line[1])
		if (usr in occurances)
			occurances[usr] += 1
		else
			occurances[usr] = 0
	}
	const sorted = Object.entries(occurances)
	sorted.sort((a, b) => b[1] - a[1])

	console.log(` ${sorted[0][0]} \n ${sorted[1][0]} \n ${sorted[2][0]}`)
})()
