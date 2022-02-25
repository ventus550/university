

function* fib() {
	p = 0; q = 1

	while (1) {
		r = p + q
		p = q; q = r
		yield p
	}
}


function* take(it, top) {
	for (let i = 0; i < top; i++) {
		yield it.next().value
	}
}


for (let num of take(fib(), 10)) {
	console.log(num);
}













