

function fibbItr(n) {
	p = 0; q = 1
	for (i = 0; i < n; i++) {
		r = p + q
		p = q; q = r
	}
	return p
}


function fibbRec(n) {
	if (n == 0 || n == 1) return n
	return fibbRec(n-1) + fibbRec(n-2)
}


function timeit(fun, n) {
	console.time("time")
	res = []
	for(m = 0; m <= n; m++) res.push( fun(m) )
	console.timeEnd("time")
	return res
}


console.log(timeit(fibbItr, 30).slice(10))
console.log(timeit(fibbRec, 30).slice(10))




// Wyniki pomiarów dla n = 30
// Chrome:
// 	fibbItr: 0.16ms
//	fibbRec: 25.2ms
// Firefox:
//	fibbItr: 1ms
//	fibbRec: 890ms
// node.js:
//	fibbItr: 0.18ms
//	fibbRec: 24.8ms