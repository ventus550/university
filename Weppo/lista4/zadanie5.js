var fs = require('fs');
fs.readFile('z5.txt', 'utf-8', function (err, data) {
	console.log(data);
});