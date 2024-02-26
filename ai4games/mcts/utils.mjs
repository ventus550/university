export function randint(a,b) {
	let n = b - a + 1
	return ~~(Math.random() * n) + a
}

export function choice(arr) {
	 let n = arr.length
	 return arr[randint(0, n-1)]
}

export function popcount(n) {
	n = n - ((n >> 1) & 0x55555555)
	n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
	return ((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) >> 24
}

export function abs2action(row, col) {
	let idx = 3*~~(row / 3) + ~~(col / 3)
	row %= 3; col %= 3
	return [idx, [row, col]]
}


export function action2abs(action) {
	let [idx, [row, col]] = action
	return [ row + 3*~~(idx / 3), col + 3*(idx % 3) ]
}


export function err(msg) {
	console.error(msg)
}
