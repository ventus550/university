
res = []
for (i = 1; i <= 100000; i++) {
	numbers = String(i).split("").map( x => Number(x) )
	sum = numbers.reduce( (a, b) => a + b )
	numbers.push(sum)

	if (numbers.every( n => i % n == 0 )) res.push(i)
}