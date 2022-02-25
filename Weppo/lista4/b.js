module.exports = { run_b };
let a = require('./a');
function run_b(n) {
	if (n < 100) {
		console.log(`b: ${n}`);
		a.run_a(2*n);
	}
}