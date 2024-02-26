// Scalar product of two vectors xs and ys
def scalarUgly(xs: List[Int], ys: List[Int]): Int = {
  var result = 0
  var i = 0
  do {
    result += xs(i) * ys(i)
    i += 1
  } while (i < xs.length && i < ys.length)
  result
}

def scalar(xs: List[Int], ys: List[Int]): Int = {
  (for ((x, y) <- xs.zip(ys)) yield x * y).sum
}

// Test the functions
val xs = List(1, 2, 3, 4, 5)
val ys = List(6, 7, 8, 9, 10)
println(s"Scalar Product: ${scalar(xs, ys)}")
println(s"Scalar Ugly Product: ${scalarUgly(xs, ys)}")
