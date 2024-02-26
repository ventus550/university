

function fibbIt() {
	p = 0; q = 1

	return {
		next: function () {
			r = p + q
			p = q; q = r

			return {
				value: p,
				done: false
			}
		}
	}
}



function* fibb() {
	p = 0; q = 1

	while (1) {
		r = p + q
		p = q; q = r
		yield p
	}
}

var _it = fibb();
for (let i = 0; i < 10; i++) {
	console.log(_it.next().value)
}

var _it = fibbIt();
for (let i = 0; i < 10; i++) {
	console.log(_it.next().value)
}
