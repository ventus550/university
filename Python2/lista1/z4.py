from random import randint


def flip(coins = 3):
	count = coins
	prev = None
	flips = 0

	while count:
		coin = randint(0, 1)
		if coin != prev:
			count = coins
		
		count -= 1
		prev = coin
		flips += 1
	
	return flips


def run(times):
	return sum(flip() for x in range(times)) / times

print(run(10000))

