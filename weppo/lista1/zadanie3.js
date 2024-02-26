
primes = []
for (i = 2; i <= 100000; i++) {
	if (primes.every( p => i % p )) primes.push(i)
}