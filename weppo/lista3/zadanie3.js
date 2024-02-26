
function forEach(a, f) {
	for (let x of a) f(x)
}


function map(a, f) {
	res = []
	forEach( a, x => res.push(f(x)) )
	return res
}


function filter(a, f) {
	res = []
	forEach( a, x => { if(f(x)) res.push(x) } )
	return res
}


let a = [1, 2, 3, 4]
forEach( a, _ => {console.log( _ )} )

console.log(filter( a, _ => _ < 3 ))

console.log(map( a, _ => _ * 2 ))