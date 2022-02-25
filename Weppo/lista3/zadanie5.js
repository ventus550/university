

function sum(...args) {
	return args.reduce( (a,x) => a + x )
}

console.assert(sum(1,2,3) === 6);
console.assert(sum(1,2,3,4,5) === 15);
