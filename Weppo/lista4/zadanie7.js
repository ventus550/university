const
fs = require('fs'),
util = require('util');


/**
 * Klasycznie
 */
fs.readFile('logs.txt', 'utf-8', function (err, data) {
	// zrób coś z data
})


/**
 * Ręcznie napisana funkcja zwracająca Promise
 */
function readFileAsync(name, encoding) {
	return new Promise((resolve, reject) => {
		fs.readFile(name, encoding, (error, data) => {
			if (error)
				reject(error)
			else
				resolve(data)
		})
	})
}
readFileAsync('logs.txt', 'utf-8').then(data => {
	// zrób coś z data
})


/**
 * util.primisify
 */
const readFilePromisified = util.promisify(fs.readFile)
readFilePromisified('logs.txt', 'utf-8').then(data => {
	// zrób coś z data
})



/**
 * fs.promises
 */
fs.promises.readFile('logs.txt', 'utf-8').then(data => {
	// zrób coś z data
});



/**
 * Jak obsłużyć funkcję zwracającą Promise przy pomocy async/await?
 */
(async function () {
	var result = await fs.promises.readFile('logs.txt', 'utf-8');
	console.log(result);
})();