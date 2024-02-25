// Quicksort algorithm
def sortUgly(xs: List[Int]): List[Int] = {

  def swap(xs: Array[Int], pos1: Int, pos2: Int): Unit = {
    val stash = xs(pos1)
    xs(pos1) = xs(pos2)
    xs(pos2) = stash
  }
  
  def partition(subArray: Array[Int], low: Int, hi: Int): Int = {
    val pivot = hi;
    var i = low;
    for (
      j <- low to hi
      if subArray(j) < subArray(pivot)
    ) {swap(subArray, i, j); i+=1}

    swap(subArray, i, pivot);
    return i
  }

  def quicksort(xs: Array[Int], low: Int, hi: Int): Unit = {
    if (low < hi) {
      val p = partition(xs, low, hi)
      quicksort(xs, low, p-1)
      quicksort(xs, p+1, hi)
    }
  }

  var sorted = xs.toArray
  quicksort(sorted, 0, sorted.length-1)
  return sorted.toList
}

def sort(xs: List[Int]): List[Int] = xs match {
  case Nil => Nil
  case pivot :: tail =>
    val (left, right) = tail.partition(_ < pivot)
    sort(left) ::: pivot :: sort(right)
}

// Test the functions
val xs = List(1, 5, 4, 2, 3)
println(s"Quicksort Ugly: ${sortUgly(xs)}")
println(s"Quicksort: ${sort(xs)}")
