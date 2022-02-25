module.exports = { run_a };
let b = require('./b');
function run_a(n) {
	if (n < 100) {
		console.log(`a: ${n}`);
		b.run_b(2*n);
	}
}