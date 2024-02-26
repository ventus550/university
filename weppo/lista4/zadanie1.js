

class Queue extends Array {
	constructor(...arr) {
		super()
		this.push(...arr)
	}

	pop() {
		return this.splice(0,1)
	}
}



class Tree {
	constructor(val, left, right) {
		this.left = left;
		this.right = right;
		this.val = val;
	}

	[Symbol.iterator] = function* () {
		const Q = new Queue(this)

		while (Q.length) {
			qp = Q.pop()
			yield qp.val

			if (qp.left) Q.push(qp.left)
			if (qp.right) Q.push(qp.right)
		}
	}
}

/*
	Jeśli użylibyśmy stosu to algorytm realizowałby przeszukiwanie wgłąb
*/