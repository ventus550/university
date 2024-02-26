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

function fibbMem(n) {
	var cache = {}

	function fibb(n) {
		if (n in cache)
			return cache[n]

		let res = null
		if (n == 0 || n == 1) res =  n
		else res = fibb(n-1) + fibb(n-2)
		cache[n] = res
		return res
	}

	return fibb(n)
	
}


function timeit(fun, n) {
	console.time("time")
	res = []
	for(m = 0; m <= n; m++) res.push( fun(m) )
	console.timeEnd("time")
	return res
}


console.log(timeit(fibbItr, 40).slice(10))
console.log(timeit(fibbRec, 40).slice(10))
console.log(timeit(fibbMem, 40).slice(10))
