// Checks if n is prime
def isPrimeUgly(n: Int): Boolean = {
  var i = 2
  if (n <= 1)
    return false
  
  while (i < n) {
    if (n % i == 0)
      return false
    i += 1
  }
  return true
}

def isPrime(n: Int): Boolean = {
  if (n <= 1) false
  else !(2 until n).exists(n % _ == 0)
}

// For a given positive integer n, find all pairs of integers i and j,
// where 1 ≤ j < i < n such that i + j is prime
def primePairsUgly(n: Int): List[(Int, Int)] = {
  var pairs: List[(Int, Int)] = Nil
  var i = 2
  do {
    var j = 1
    do {
      if (isPrimeUgly(i + j) && i > j) {
        pairs = (i, j) :: pairs
      }
      j += 1
    } while (j < i)
    i += 1
  } while (i < n)
  pairs.reverse
}

def primePairs(n: Int): List[(Int, Int)] = {
  for {
    i <- 2 until n
    j <- 1 until i
    if isPrime(i + j)
  } yield (i, j)
}.toList


// Test the functions
println(s"Is 7 Prime Ugly: ${isPrimeUgly(7)}")
println(s"Is 7 Prime: ${isPrime(7)}")

// Test the functions
println(s"Prime Pairs Ugly: ${primePairsUgly(10)}")
println(s"Prime Pairs: ${primePairs(10)}")
